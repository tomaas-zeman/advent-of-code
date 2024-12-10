declare global {
  interface Array<T> {
    asInt: () => number[];
    get: (number) => T;
  }
}

export {};
