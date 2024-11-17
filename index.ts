import process from 'process';
import yargs from 'yargs';
import fs from 'fs';
import color from 'cli-color';
import readline from 'readline';
import './polyfills';

type Solver = typeof import('./day_template_ts/part1');

const ANSWERS_FILE_PATH = './answers.txt';
const SESSION = fs.readFileSync('.session', 'utf-8').trim();

function parseArgs() {
  return yargs(process.argv)
    .options({
      year: { type: 'string', demandOption: true },
      day: { type: 'string', demandOption: true },
      partOverride: { type: 'string' },
    })
    .parse();
}

async function ensureRealInputFile(year: string, day: string) {
  const file = `year${year}/day${day}/data`;

  if (fs.existsSync(file)) {
    return;
  }

  const response = await fetch(`https://adventofcode.com/${year}/day/${parseInt(day, 10)}/input`, {
    headers: {
      Cookie: `session=${SESSION}`,
    },
  });

  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }

  const body = (await response.text()).trim();
  fs.writeFileSync(file, body);
}

function readInputFile(year: string, day: string, file: string, part = '') {
  let path = `./year${year}/day${day}/${file}`;
  if (!fs.existsSync(path)) {
    path += part;
  }
  return fs.readFileSync(path, 'utf-8').split('\n');
}

async function getTestInput(year: string, day: string, part: string) {
  return readInputFile(year, day, 'testdata', part);
}

async function getRealInput(year: string, day: string) {
  await ensureRealInputFile(year, day);
  return readInputFile(year, day, 'data');
}

function saveCorrectAnswer(year: string, day: string, part: string, answer: string | number) {
  const line = `${year}-${day}-${part}=${answer}\n`;
  fs.appendFileSync(ANSWERS_FILE_PATH, line, 'utf-8');
}

function getCorrectAnswer(year: string, day: string, part: string) {
  const data = fs.readFileSync(ANSWERS_FILE_PATH, 'utf-8');
  const lines = data.split('\n');
  for (const line of lines) {
    if (line.startsWith(`${year}-${day}-${part}=`)) {
      return line.split('=')[1].trim();
    }
  }
}

async function sendAnswer(year: string, day: string, part: string, answer: string | number) {
  const correctAnswer = getCorrectAnswer(year, day, part);
  if (correctAnswer) {
    if (correctAnswer == answer) {
      console.log(color.yellow('> You already submitted a correct answer for this part.'));
    } else {
      console.log(
        color.red("> You already submitted a correct answer for this part but it's incorrect NOW"),
      );
    }
    return;
  }

  const prompt = readline.createInterface({ input: process.stdin, output: process.stdout });
  const choice = await new Promise<string>((resolve) => {
    prompt.question(`> Send answer '${answer}' to AOC for verification? [y/N] `, (answer) => {
      prompt.close();
      resolve(answer);
    });
  });
  if (choice.toLowerCase() !== 'y') {
    return;
  }

  const response = await fetch(`https://adventofcode.com/${year}/day/${parseInt(day, 10)}/answer`, {
    headers: { Cookie: `session=${SESSION}`, 'Content-Type': 'application/x-www-form-urlencoded' },
    method: 'POST',
    body: new URLSearchParams({ level: part, answer: answer.toString() }).toString(),
  });

  if (!response.ok) {
    throw new Error(`Failed to submit the answer: ${response.status} ${response.statusText}`);
  }

  const responseText = await response.text();

  if (responseText.includes('You gave an answer too recently')) {
    console.log(color.red('> You submitted an answer too recently. Try again in a few minutes.'));
  } else if (responseText.includes('not the right answer')) {
    if (responseText.includes('too low')) {
      console.log(color.red('> Incorrect answer - too low.'));
    } else if (responseText.includes('too high')) {
      console.log(color.red('> Incorrect answer - too high.'));
    } else {
      console.log(color.red('> Incorrect answer'));
    }

    const waitBeforeRetry = responseText.match(/([Pp]lease wait .*? trying again\.)/);
    if (waitBeforeRetry) {
      console.log(color.yellow(`> ${waitBeforeRetry[1]}`));
    }
  } else if (responseText.includes('seem to be solving the right level.')) {
    console.log(color.yellow('> Wrong level or already solved.'));
  } else {
    console.log(color.green('> CORRECT!'));
    saveCorrectAnswer(year, day, part, answer);
  }
}

async function run() {
  const { year, day, partOverride } = await parseArgs();

  for (let part of partOverride ? [partOverride] : ['1', '2']) {
    console.log(color.cyan.bold('\n##################################'));
    console.log(color.cyan.bold(`#             PART ${part}             #`));
    console.log(color.cyan.bold('##################################\n'));

    const solver: Solver = await import(`./year${year}/day${day}/part${part}.ts`);

    const start = new Date().getTime();
    const testResult = solver.run(await getTestInput(year, day, part), true);
    if (testResult != solver.testResult) {
      console.error(color.red(`✘ year ${year} | day ${day} | part ${part} => ${testResult}`));
      console.error(color.yellow(`> Expected result: ${solver.testResult}`));
      return;
    }

    const result = solver.run(await getRealInput(year, day), false);
    console.log(color.green(`✔ year ${year} | day ${day} | part ${part} => ${result}`));

    const stop = new Date().getTime();
    console.log(`> Computation took ${(stop - start) / 1000} seconds`);

    await sendAnswer(year, day, part, result);
  }
}

run();
