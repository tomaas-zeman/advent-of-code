//--------------------
//     UTILITIES     -
//--------------------

export type Node = [number, number];
export type Point = Node;

// Modulo that produces positive results for negative numbers.
// For example -3 mod 5 = 2
export function mod(number: number, base: number) {
  return ((number % base) + base) % base;
}

export class TypeGuard {
  static isFunction(variable: any): variable is Function {
    return typeof variable === 'function';
  }

  static isNumber(variable: any): variable is number {
    return typeof variable === 'number';
  }

  static isArray<T>(variable: any): variable is Array<T> {
    return Array.isArray(variable);
  }

  static isTuple<T>(variable: any): variable is [T, T] {
    return Array.isArray(variable) && variable.length === 2;
  }
}

//-----------------
//     ARRAYS     -
//-----------------

export function sum(arr: number[]): number {
  return arr.reduce((sum, n) => sum + n, 0);
}

export function pairwise<T>(arr: T[], length = 2): T[][] {
  const pairs: T[][] = [];
  for (let i = 0; i < arr.length - (length - 1); i++) {
    pairs.push(arr.slice(i, i + length));
  }
  return pairs;
}

// Significantly faster than lodash/isEqual
export function isEqual<T>(a: T[], b: T[]) {
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) {
      return false;
    }
  }
  return true;
}
