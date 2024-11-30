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

export const instructions: { [name: string]: Instruction } = {
  addr: new Addr(),
  addi: new Addi(),
  mulr: new Mulr(),
  muli: new Muli(),
  banr: new Banr(),
  bani: new Bani(),
  borr: new Borr(),
  bori: new Bori(),
  setr: new Setr(),
  seti: new Seti(),
  gtir: new Gtir(),
  gtri: new Gtri(),
  gtrr: new Gtrr(),
  eqir: new Eqir(),
  eqri: new Eqri(),
  eqrr: new Eqrr(),
};
