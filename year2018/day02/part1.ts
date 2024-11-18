import { Config } from "../..";

export async function run(data: string[], config: Config): Promise<string | number> {
  const counts = data.reduce<{ [key: string]: number }[]>((result, word) => {
    const count = word.split('').reduce<{ [key: string]: number }>((acc, letter) => {
      if (!acc[letter]) {
        acc[letter] = 0;
      }
      acc[letter]++;
      return acc;
    }, {});

    result.push(count);
    return result;
  }, []);

  const twos = counts.filter((count) => Object.values(count).includes(2)).length;
  const threes = counts.filter((count) => Object.values(count).includes(3)).length;
  return twos * threes;
}

export const testResult = 12;
