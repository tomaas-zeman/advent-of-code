export function run(data: string[]): string | number {
  const frequencies = new Set();

  let frequency = 0;
  let i = 0;
  while (true) {
    frequency += parseInt(data[i % data.length]);
    if (frequencies.has(frequency)) {
      return frequency;
    }
    frequencies.add(frequency);
    i++;
  }
}

export const testResult = 2;
