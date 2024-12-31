type Operation = (a: number, b: number) => number;
type Condition = (a: number, b: number) => boolean;

export type Instruction = {
  register: string;

  operation: Operation;
  operationValue: number;

  condition: Condition;
  conditionRegisterA: string;
  conditionValueB: number;
};

export const operations: Record<string, Operation> = {
  inc: (a, b) => a + b,
  dec: (a, b) => a - b,
};

export const conditions: Record<string, Condition> = {
  '<': (a, b) => a < b,
  '>': (a, b) => a > b,
  '==': (a, b) => a === b,
  '!=': (a, b) => a !== b,
  '<=': (a, b) => a <= b,
  '>=': (a, b) => a >= b,
};

export function parse(data: string[]) {
  const instructions: Instruction[] = [];
  const pattern = /(\w+) (inc|dec) (-?\d+) if (\w+) ([=<>!]+) (-?\d+)/;

  for (const line of data) {
    const [
      _,
      register,
      operation,
      operationValue,
      conditionRegisterA,
      condition,
      conditionValueB,
    ] = line.match(pattern)!;
    instructions.push({
      register,
      operation: operations[operation],
      operationValue: parseInt(operationValue),
      condition: conditions[condition],
      conditionRegisterA,
      conditionValueB: parseInt(conditionValueB),
    });
  }

  return instructions;
}
