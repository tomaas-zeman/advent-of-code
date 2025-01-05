import { Config } from '../..';
import { Command, Computer } from './common';

// Yet another piece of shit assembler reverse engineering :X
//
// 01: set a 1
//     ...
// 09: set f 1
// => all is just program init
// => the important bit is setting 'b' and 'c' which is N*17 apart and is the loop range
// => we can set 'b' and 'c' to arbitrary numbers and if they keep the N*17 difference,
//    the loop will always end (infinite loop otherwise)
//
// 10: set d 2
// ...
// 12: set g d
// 13: mul g e
// 14: sub g b
// => (d * e) - b essentially checks if b == d * e, e.i. if 'b' is composed of 'd' and 'e'
// => if it is, we set f = 0
//
// 18: set g e
// 19: sub g b
// 20: jnz g -8
// => basically loop range check - we always iterate e..b before moving on
// => this repeats on lines 22-24 with d..b check
// => IOW: two nested loop producing all numbers between e..b/d..b and checking if 'b' is composed from them (not a prime)
//
// 25: jnz f 2
// 26: sub h -1
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// => if we found in the loops above that 'b' is composed from 'e' and 'd', we can increment 'h' !
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//     ...
// 27: set g b
// 28: sub g c
// 29: jnz g 2
// => this is the loop range check
//     ...
// 31: sub b -17
// 32: jnz 1 -23
// => here is the 'b' + 17 step increment and jump that takes us back to line 10
export async function run(data: string[], config: Config): Promise<string | number> {
  const computer = new Computer();
  computer.registers.set('a', 1);

  let counter = 0;

  while (computer.ip < data.length) {
    const ip = computer.ip;
    const [instruction, register, value] = data[computer.ip].split(' ') as Command;
    computer.processInstruction(instruction, register, value);

    // Initialization completed - calculate 'h'
    if (computer.ip === 9) {
      for (let n = computer.registers.get('b'); n <= computer.registers.get('c'); n += 17) {
        // Really inefficient way to check if 'n' is not a prime
        // for (let a = 2; a <= n; a++) {
        //   for (let b = 2; b <= n; b++) {
        //     if (a * b === n) {
        //       counter++;
        //     }
        //   }
        // }
        if (!isPrime(n)) {
          counter++;
        }
      }
      break;
    }
  }

  return counter;
}

// https://stackoverflow.com/questions/62150130/algorithm-of-checking-if-the-number-is-prime
function isPrime(n: number) {
  for (let i = 2, s = Math.sqrt(n); i <= s; i++) {
    if (n % i === 0) return false;
  }
  return n > 1;
}

export const testResult = 3;
