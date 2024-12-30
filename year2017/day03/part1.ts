import { Config } from '../..';

// 37	36	35	34	33	32	31
// 38	17	16	15	14	13	30
// 39	18	 5	 4	 3	12	29
// 40	19	 6	 1	 2	11	28
// 41	20	 7 	 8	 9	10	27
// 42	21	22	23	24	25	26
// 43	44	45	46	47	48	49
//
// Highest number in each layer L is a n^2 where n is 1,3,5,7,...
function getDistanceFromCenter(n: number) {
  const layer = Math.ceil((Math.sqrt(n) - 1) / 2);
  const size = 1 + layer * 2;
  const first = Math.pow(size - 2, 2) + 1;
  const last = Math.pow(size, 2);

  const sides = [
    [first, first + size - 3],
    [first + size - 2, first + 2 * size - 3],
    [first + 2 * size - 2, first + 3 * size - 5],
    [first + 3 * size - 4, last],
  ];

  for (const [from, to] of sides) {
    if (n >= from && n <= to) {
      const sideCenter = from + (to - from) / 2;
      const distanceFromSideCenter = Math.abs(sideCenter - n);
      return distanceFromSideCenter + layer;
    }
  }

  throw new Error("Shouldn't happen");
}

export async function run(data: string[], config: Config): Promise<string | number> {
  return getDistanceFromCenter(parseInt(data[0]));
}

export const testResult = 31;
