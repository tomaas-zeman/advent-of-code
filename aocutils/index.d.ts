declare global {
  interface Array<T> {
    asInt: () => number[];
  }
}

export {};
