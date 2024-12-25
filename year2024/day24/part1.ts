import { Config } from '../..';
import fs from 'fs';
import os from 'os';
import path from 'path';
import { execSync } from 'child_process';

function composeInput(match: RegExpMatchArray) {
  const [_, wire, value] = match;
  return `const ${wire} = () => ${value};\n`;
}

function composeGate(match: RegExpMatchArray) {
  const [_, in1, gate, in2, out] = match;
  return `const ${out} = () => ${gate}(${in1}(), ${in2}());\n`;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const runnableFile = path.join(os.tmpdir(), 'aoc-2024-24-01.js');
  fs.writeFileSync(runnableFile, ''); // clear file

  const processors: [RegExp, (match: RegExpMatchArray) => string][] = [
    [/(\w{3}): (\d)/, composeInput],
    [/(\w{3}) (AND|OR|XOR) (\w{3}) -> (\w{3})/, composeGate],
  ];

  for (const line of data) {
    for (const [regex, handler] of processors) {
      const match = line.match(regex);
      if (match) {
        fs.appendFileSync(runnableFile, handler(match));
        break;
      }
    }
  }

  fs.appendFileSync(runnableFile, `
    // Gates
    const AND = (a, b) => (a == 1 && b == 1 ? 1 : 0);
    const XOR = (a, b) => (a != b ? 1 : 0);
    const OR = (a, b) => (a == 1 || b == 1 ? 1 : 0);

    // Dynamically evaluate all output wires and send the result to stdout
    let result = '';
    for (let i = 0; i <= ${config.isTest ? 12 : 45}; i++) {
      result += eval(\`z\${i.toString().padStart(2, '0')}()\`);
    }

    console.log(parseInt(result.split('').toReversed().join(''), 2));
  `);

  const runner = execSync(`${process.execPath} ${runnableFile}`);
  return runner.toString().trim();
}

export const testResult = '2024';
