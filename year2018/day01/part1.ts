export function run(data: string[]): string | number {
  return data.reduce((acc, value) => acc + parseInt(value), 0);
}

export const testResult = 3;
