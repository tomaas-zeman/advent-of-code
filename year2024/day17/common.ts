export type Registers = [bigint, bigint, bigint];

export class Computer {
  ip: number = 0;
  output: number[] = [];

  private registers: Registers;
  private opcodes = [
    this.adv,
    this.bxl,
    this.bst,
    this.jnz,
    this.bxc,
    this.out,
    this.bdv,
    this.cdv,
  ];

  constructor(registers: Registers) {
    this.registers = registers;
  }

  process(opcode: number, operand: number) {
    this.opcodes[opcode].call(this, operand);
    if (opcode !== 3 || this.registers[0] === 0n) {
      this.ip += 2;
    }
  }

  combo(operand: number) {
    if (operand >= 7) {
      throw new Error('Unsupported operand!');
    }
    return operand <= 3 ? BigInt(operand) : this.registers[operand - 4];
  }

  adv(operand: number) {
    this.registers[0] >>= this.combo(operand);
  }

  bxl(operand: number) {
    this.registers[1] ^= BigInt(operand);
  }

  bst(operand: number) {
    this.registers[1] = this.combo(operand) & 0b111n;
  }

  jnz(operand: number) {
    if (this.registers[0] !== 0n) {
      this.ip = operand;
    }
  }

  bxc(_: number) {
    this.registers[1] ^= this.registers[2];
  }

  out(operand: number) {
    this.output.push(parseInt(this.combo(operand).toString()) & 0b111);
  }

  bdv(operand: number) {
    this.registers[1] = this.registers[0] >> this.combo(operand);
  }

  cdv(operand: number) {
    this.registers[2] = this.registers[0] >> this.combo(operand);
  }
}

export function parse(data: string[]): [Registers, number[]] {
  const registers = [
    ...data
      .slice(0, 3)
      .join('')
      .match(/(\d+)/g)!
      .map((v) => BigInt(v)),
    0n,
  ] as Registers;
  const program = data.get(-1).split(' ')[1].split(',').asInt();
  return [registers, program];
}
