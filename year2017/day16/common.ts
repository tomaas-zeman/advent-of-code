import range from 'lodash/range';
import { Config } from '../..';
import { DefaultMap } from '../../aocutils';

export function init(data: string[], config: Config): [string[], string[]] {
  const instructions = data[0].split(',');
  let programs = range(0, config.isTest ? 5 : 16).map((offset) =>
    String.fromCharCode('a'.charCodeAt(0) + offset),
  );
  return [instructions, programs];
}

function swap(programs: string[], i: number, j: number) {
  const tmp = programs[i];
  programs[i] = programs[j];
  programs[j] = tmp;
}

export function dance(instructions: string[], programs: string[], maxRepeats: number) {
  const cache = new DefaultMap<string, number>(0);

  for (let repeats = 0; repeats < maxRepeats; repeats++) {
    for (const instr of instructions) {
      if (instr.startsWith('s')) {
        const n = parseInt(instr.substring(1));
        programs = [...programs.slice(-n), ...programs.slice(0, -n)];
      } else if (instr.startsWith('x')) {
        const [i, j] = instr.substring(1).split('/').asInt();
        swap(programs, i, j);
      } else if (instr.startsWith('p')) {
        const [i, j] = instr
          .substring(1)
          .split('/')
          .map((c) => programs.indexOf(c));
        swap(programs, i, j);
      }
    }

    const result = programs.join('');
    if (cache.has(result)) {
      const period = repeats - cache.get(result);
      repeats += Math.floor((maxRepeats - repeats) / period) * period;
    }

    cache.set(result, repeats);
  }

  return programs.join('');
}
