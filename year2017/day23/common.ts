import { DefaultMap } from '../../aocutils';

export type Instruction = 'jnz' | 'set' | 'sub' | 'mul';
export type Command = [Instruction, string, string];

export class Computer {
  ip = 0;
  mulCount = 0;
  registers = new DefaultMap<string, number>(0);

  private instructions = {
    jnz: (register: string, value: string) => {
      this.ip += this.getValue(register) !== 0 ? this.getValue(value) : 1;
    },
    set: (register: string, value: string) => {
      this.registers.set(register, this.getValue(value));
      this.ip++;
    },
    sub: (register: string, value: string) => {
      this.registers.mapItem(register, (v) => v - this.getValue(value));
      this.ip++;
    },
    mul: (register: string, value: string) => {
      this.registers.mapItem(register, (v) => v * this.getValue(value));
      this.ip++;
      this.mulCount++;
    },
  };

  processInstruction(instruction: Instruction, register: string, value: string) {
    this.instructions[instruction](register, value);
  }

  private getValue(registerOrValue: string) {
    if (registerOrValue.match(/\d+/)) {
      return parseInt(registerOrValue);
    }
    return this.registers.get(registerOrValue);
  }
}
