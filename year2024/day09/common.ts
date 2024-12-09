export type FS = (number | null)[];

export function parse(data: string[]): [FS, number] {
  const fs = [];

  let blockId = 0;
  for (let i = 0; i < data[0].length; i++) {
    const size = parseInt(data[0][i]);
    if (i % 2 === 0) {
      fs.push(...new Array(size).fill(blockId++));
    } else {
      fs.push(...new Array(size).fill(null));
    }
  }

  return [fs, blockId - 1];
}

export function computeCheckSum(fs: FS): string | number | PromiseLike<string | number> {
  return fs.reduce<number>((sum, id, index) => (id == null ? sum : sum + id * index), 0);
}
