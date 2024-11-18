import process from 'process';
import yargs from 'yargs';
import fs from 'fs';
import color from 'cli-color';
import { fetchInputData } from './ts-runner/aocapi';
import { sendAnswer } from './ts-runner/answers';
import { Visualization, NoVisualization } from './ts-runner/visualization';
import './polyfills';

type Solver = typeof import('./templates/day_template_ts/part1');

function parseArgs() {
  return yargs(process.argv)
    .options({
      year: { type: 'string', demandOption: true },
      day: { type: 'string', demandOption: true },
      partOverride: { type: 'string' },
      visualization: { type: 'boolean' },
    })
    .default('visualization', false)
    .parse();
}

export type Config = {
  year: string;
  day: string;
  part: string;
  visualization: Visualization | NoVisualization;
  isTest: boolean;
};

async function ensureRealInputFile(year: string, day: string) {
  const file = `year${year}/day${day}/data`;

  if (fs.existsSync(file)) {
    return;
  }

  const response = await fetchInputData(year, day);
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

function createConfig(
  year: string,
  day: string,
  part: string,
  visualization: boolean,
  isTest: boolean,
) {
  const config: Config = { year, day, part, isTest, visualization: new NoVisualization() };
  if (visualization) {
    config.visualization = new Visualization(config);
  }
  return config;
}

async function run() {
  const { year, day, partOverride, visualization } = await parseArgs();

  for (let part of partOverride ? [partOverride] : ['1', '2']) {
    console.log(color.cyan.bold('\n##################################'));
    console.log(color.cyan.bold(`#             PART ${part}             #`));
    console.log(color.cyan.bold('##################################\n'));

    const solver: Solver = await import(`./year${year}/day${day}/part${part}.ts`);

    const start = new Date().getTime();
    const testResult = await solver.run(
      await getTestInput(year, day, part),
      createConfig(year, day, part, visualization, true),
    );
    if (testResult != solver.testResult) {
      console.error(color.red(`✘ year ${year} | day ${day} | part ${part} => ${testResult}`));
      console.error(color.yellow(`> Expected result: ${solver.testResult}`));
      return;
    }

    const result = await solver.run(
      await getRealInput(year, day),
      createConfig(year, day, part, visualization, false),
    );
    console.log(color.green(`✔ year ${year} | day ${day} | part ${part} => ${result}`));

    const stop = new Date().getTime();
    console.log(`> Computation took ${(stop - start) / 1000} seconds`);

    await sendAnswer(year, day, part, result);
  }
}

run();
