class Sample {
  id: number;
  before: number[];
  after: number[];
  opcode: number;
  a: number;
  b: number;
  c: number;

  constructor(
    id: number,
    before: number[],
    after: number[],
    opcode: number,
    a: number,
    b: number,
    c: number,
  ) {
    this.id = id;
    this.before = before;
    this.after = after;
    this.opcode = opcode;
    this.a = a;
    this.b = b;
    this.c = c;
  }
}

class Operation {
  opcode: number;
  a: number;
  b: number;
  c: number;

  constructor(opcode: number, a: number, b: number, c: number) {
    this.opcode = opcode;
    this.a = a;
    this.b = b;
    this.c = c;
  }
}

export function parseInput(data: string[]): [Sample[], Operation[]] {
  const samples: Sample[] = [];
  const operations: Operation[] = [];

  for (let i = 0; i < data.length; i++) {
    if (!data[i].trim()) {
      continue;
    }
    if (data[i].startsWith('Before')) {
      const before = eval(data[i].split(': ')[1]) as number[];
      const after = eval(data[i + 2].split(': ')[1]) as number[];
      const [opcode, a, b, c] = data[i + 1].split(' ').map((value) => parseInt(value));
      samples.push(new Sample(samples.length, before, after, opcode, a, b, c));
      i += 2;
    } else {
      const [opcode, a, b, c] = data[i].split(' ').map((value) => parseInt(value));
      operations.push(new Operation(opcode, a, b, c));
    }
  }

  return [samples, operations];
}

export interface Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[];
}

class Addr implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] + registers[b];
    return result;
  }
}

class Addi implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] + b;
    return result;
  }
}

class Mulr implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] * registers[b];
    return result;
  }
}

class Muli implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] * b;
    return result;
  }
}

class Banr implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] & registers[b];
    return result;
  }
}

class Bani implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] & b;
    return result;
  }
}

class Borr implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] | registers[b];
    return result;
  }
}

class Bori implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] | b;
    return result;
  }
}

class Setr implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a];
    return result;
  }
}

class Seti implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = a;
    return result;
  }
}

class Gtir implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = a > registers[b] ? 1 : 0;
    return result;
  }
}

class Gtri implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] > b ? 1 : 0;
    return result;
  }
}

class Gtrr implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] > registers[b] ? 1 : 0;
    return result;
  }
}

class Eqir implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = a === registers[b] ? 1 : 0;
    return result;
  }
}

class Eqri implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] === b ? 1 : 0;
    return result;
  }
}

class Eqrr implements Instruction {
  eval(registers: number[], a: number, b: number, c: number): number[] {
    const result = [...registers];
    result[c] = registers[a] === registers[b] ? 1 : 0;
    return result;
  }
}

export const instructions: Instruction[] = [
  new Addr(),
  new Addi(),
  new Mulr(),
  new Muli(),
  new Banr(),
  new Bani(),
  new Borr(),
  new Bori(),
  new Setr(),
  new Seti(),
  new Gtir(),
  new Gtri(),
  new Gtrr(),
  new Eqir(),
  new Eqri(),
  new Eqrr(),
];

export function arraysEqual(arr1: number[], arr2: number[]) {
  if (arr1.length !== arr2.length) {
    return false;
  }
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }
  return true;
}
