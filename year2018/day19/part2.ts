import { Config } from '../..';
import { Instruction, instructions } from './../day16/common';

//     THE MAIN SUBLOOP
//
//     assembly      pseudocode
//     ------------+-----------
//00   addi 1 16 1   ip += 16
//01   seti 1 8 2    r2 = 1
//02 F:seti 1 5 4    r4 = 1
//
//03 D:mulr 2 4 3    r3 = r2 * r4
//04   eqrr 3 5 3    if (r3 == r5)
//05   addr 3 1 1    ip += r3
//06   addi 1 1 1    ip += 1
//     =>  if (r2 * r4 == r5)
//           goto A
//         else
//           goto B
//
//07 A:addr 2 0 0    r0 += r2  // result register
//08 B:addi 4 1 4    r4 += 1
//09   gtrr 4 5 3    if (r4 > r5)
//10   addr 1 3 1    ip += r3
//11   seti 2 8 1    ip = 2
//     =>  if (r4 > r5)
//           goto C
//         else
//           goto D
//
//12 C:addi 2 1 2    r2 += 1
//13   gtrr 2 5 3    if (r2 > r5)
//14   addr 3 1 1    ip += r3
//15   seti 1 8 1    ip = 1
//16 E:mulr 1 1 1    ip = ip * ip
//     =>  if (r2 > r5)
//           goto E
//         else
//           goto F
export async function run(data: string[], config: Config): Promise<string | number> {
  let registers = [1, 0, 0, 0, 0, 0];
  const program: [Instruction, number, number, number][] = data.slice(1).map((line) => {
    const [instruction, a, b, c] = line.split(' ');
    return [instructions[instruction], parseInt(a), parseInt(b), parseInt(c)];
  });

  let ipRegister = parseInt(data[0].slice(-1));
  let ipValue = 0;

  while (true) {
    registers[ipRegister] = ipValue;

    if (ipValue === 3 && registers[2] !== 0) {
      if (registers[5] % registers[2] === 0) {
        registers[0] += registers[2];
      }
      registers[3] = 0;
      registers[4] = registers[5];
      ipValue = 12;
      continue;
    }

    const [instruction, a, b, c] = program[ipValue];
    registers = instruction.eval(registers, a, b, c);

    ipValue = registers[ipRegister];
    ipValue++;

    if (ipValue >= program.length) {
      break;
    }
  }

  return registers[0];
}

export const testResult = 6;
