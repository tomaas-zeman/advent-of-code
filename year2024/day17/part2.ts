import { Config } from '../..';
import { isEqual } from '../../aocutils';
import { Computer, parse, Registers } from './common';

// The whole program
//
// bst 4  : r1 := r0 and 0b111 (mod 8)
// bxl 4  : r1 := r1 xor 0b100
// cdv 5  : r2 := r0 rshift r1
// bxc 1  : r1 := r1 xor r2
// bxl 4  : r1 := r1 xor 0b100
// out 5  : write r1
// adv 3  : r0 := r0 rshift 3
// jnz 0  : goto 0 if r0 == 0
// => each cycle starts with lowest three bits
// => each cycle ends with r0 == 0
// => each cycle we also rshift the number by three bits
//
// This means we should be able to just infer the number and it should be 3x16 bits long
// where 16 is the length of our puzzle input.
//
// Additionally, it turned out that there is some currying going on so it cannot be done
// forwards but rather backwards :X

function isInvalidNumber(program: number[], output: number[]) {
  if (output.length > program.length) {
    return true;
  }
  for (let i = 0; i < output.length; i++) {
    if (output[i] !== program[i]) {
      return true;
    }
  }
  return false;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  if (config.isTest) {
    return 0;
  }

  const [registers, program] = parse(data);

  // Smallest number I was able to manually infer from the rules above by going backwards.
  // I was changing 3 bits (all combinations) until I got the desired number, then moving 3 bits
  // to the right and so on.
  //
  // After this number, I started to get multiple options but it's now at least feasible to bruteforce.
  const min = 0b000100011101100011011111110110000000000000000000000n;
  const max = 0b000100011101100011011111110111111111111111111111111n;

  for (let value = min; value <= max; value++) {
    const comp = new Computer([value, ...registers.slice(1)] as Registers);

    while (comp.ip < program.length) {
      const opcode = program[comp.ip];
      const operand = program[comp.ip + 1];
      comp.process(opcode, operand);

      if (isInvalidNumber(program, comp.output)) {
        break;
      }

      if (isEqual(program, comp.output)) {
        return value.toString();
      }
    }
  }

  throw new Error('Solution not found!');
}

export const testResult = 0;
