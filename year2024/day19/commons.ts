export function parse(data: string[]): [string[], string[]] {
  const towels = data[0].split(', ');
  const designs = data.slice(2);
  return [towels, designs];
}

export function countValidCombinations(towels: string[]) {
  const cache: Record<string, number> = {};

  return function slice(design: string) {
    if (design.length === 0) {
      return 1;
    }

    if (cache[design]) {
      return cache[design];
    }

    let counter = 0;
    for (const towel of towels) {
      if (design.startsWith(towel)) {
        counter += slice(design.slice(towel.length));
      }
    }

    cache[design] = counter;
    return counter;
  };
}
