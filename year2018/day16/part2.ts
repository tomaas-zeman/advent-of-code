import { Config } from '../..';
import { arraysEqual } from '../../aocutils';
import { Instruction, parseInput } from './common';
import { instructions } from './common';

const OPCODES_COUNT = 16;

export async function run(data: string[], config: Config): Promise<string | number> {
  if (config.isTest) {
    return 0;
  }

  const [samples, operations] = parseInput(data);

  // Group instructions by possible opcodes
  const opcodeInstruction: { [opcode: number]: Set<Instruction> } = new Array(OPCODES_COUNT)
    .fill(0)
    .reduce((acc, _, opcode) => {
      acc[opcode] = new Set();
      return acc;
    }, {});

  for (let sample of samples) {
    for (let instruction of Object.values(instructions)) {
      const result = instruction.eval(sample.before, sample.a, sample.b, sample.c);
      const expectedResult = sample.after;
      if (arraysEqual(result, expectedResult)) {
        opcodeInstruction[sample.opcode].add(instruction);
      }
    }
  }

  // Iteratively remove instructions that have unique opcode from
  // other opcodes to create unique mapping of 1 opcode -> 1 instruction
  const opcodesProcessed: string[] = [];
  while (opcodesProcessed.length != OPCODES_COUNT) {
    const unusedOpcodeWithSingleInstruction = Object.entries(opcodeInstruction).find(
      ([opcode, instructions]) => !opcodesProcessed.includes(opcode) && instructions.size === 1,
    );

    if (!unusedOpcodeWithSingleInstruction) {
      break;
    }

    const opcode = unusedOpcodeWithSingleInstruction[0];
    const instruction = [...unusedOpcodeWithSingleInstruction[1]][0];

    for (let key of Object.keys(opcodeInstruction)) {
      if (key === opcode) {
        continue;
      }
      opcodeInstruction[key].delete(instruction);
    }

    opcodesProcessed.push(opcode);
  }

  // Run the program and compute the result
  let registers = [0, 0, 0, 0];
  for (let operation of operations) {
    const instruction = [...opcodeInstruction[operation.opcode]][0];
    registers = instruction.eval(registers, operation.a, operation.b, operation.c);
  }

  return registers[0];
}

export const testResult = 0;
