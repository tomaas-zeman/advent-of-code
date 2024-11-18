import { Config } from "../..";

export async function run(data: string[], config: Config): Promise<string | number> {
  for (let i = 0; i < data.length - 1; i++) {
    const word = data[i];

    for (let j = i + 1; j < data.length; j++) {
      const nextWord = data[j];
      const differentLetterIndexes: number[] = [];

      for (let k = 0; k < word.length; k++) {
        if (word[k] !== nextWord[k]) {
          differentLetterIndexes.push(k);
        }
      }

      if (differentLetterIndexes.length == 1) {
        return word.slice(0, differentLetterIndexes[0]) + word.slice(differentLetterIndexes[0] + 1);
      }
    }
  }

  throw new Error('No words with difference 1 found!');
}

export const testResult = 'fgij';
