//--------------------
//     UTILITIES     -
//--------------------

export type Node = [number, number];
export type Point = Node;
export type Point3D = [number, number, number];
export type Point4D = [number, number, number, number];

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

export function nwise<T>(arr: T[], length = 2): T[][] {
  const tuples: T[][] = [];
  for (let i = 0; i < arr.length - (length - 1); i++) {
    tuples.push(arr.slice(i, i + length));
  }
  return tuples;
}

export function rotate<T>(arr: T[], times = 1, reverse = false): T[] {
  if (arr.length === 0) {
    return arr;
  }
  for (let i = 0; i < times; i++) {
    if (reverse) {
      arr.unshift(arr.pop()!);
    } else {
      arr.push(arr.shift()!);
    }
  }
  return arr;
}

// Significantly faster than lodash/isEqual
export function isEqual<T>(a: T[], b: T[]) {
  if (a.length !== b.length) {
    return false;
  }
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) {
      return false;
    }
  }
  return true;
}

export function manhattan(a: Point | Point3D | Point4D, b: Point | Point3D | Point4D) {
  return a.reduce((sum, _, i) => sum + Math.abs(a[i] - b[i]), 0);
}
