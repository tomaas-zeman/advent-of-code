import fs from 'fs';
import color from 'cli-color';
import readline from 'readline';
import { postAnswer } from './aocapi';

const ANSWERS_FILE_PATH = './answers.txt';

export function saveCorrectAnswer(
  year: string,
  day: string,
  part: string,
  answer: string | number,
) {
  const line = `${year}-${day}-${part}=${answer}\n`;
  fs.appendFileSync(ANSWERS_FILE_PATH, line, 'utf-8');
}

export function getCorrectAnswer(year: string, day: string, part: string) {
  const data = fs.readFileSync(ANSWERS_FILE_PATH, 'utf-8');
  const lines = data.split('\n');
  for (const line of lines) {
    if (line.startsWith(`${year}-${day}-${part}=`)) {
      return line.split('=')[1].trim();
    }
  }
}

export async function sendAnswer(year: string, day: string, part: string, answer: string | number) {
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

  const response = await postAnswer(year, day, part, answer.toString());
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
