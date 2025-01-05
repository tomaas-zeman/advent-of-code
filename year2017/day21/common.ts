import { Matrix } from '../../aocutils';

const DEFAULT = '.#./..#/###'.split('/').map((row) => row.split(''));

export function parse(data: string[]) {
  const patterns = Object.fromEntries(data.map((line) => line.split(' => '))) as Record<
    string,
    string
  >;

  for (const [from, to] of Object.entries(patterns)) {
    const rotations = [new Matrix(from.split('/').map((line) => line.split('')))];
    for (let _ = 0; _ < 3; _++) {
      rotations.push(rotations.get(-1).rotate());
    }
    const variants = [
      ...rotations,
      ...rotations.flatMap((r) => [r.flipHorizontally(), r.flipVertically()]),
    ];
    for (const variant of variants) {
      patterns[variant.hash()] = to;
    }
  }

  return patterns;
}

export function runFractalEnhancement(mapping: Record<string, string>, iterations: number) {
  let image = new Matrix<string>(DEFAULT);

  for (let iteration = 0; iteration < iterations; iteration++) {
    image = enhanceImage(image, mapping);
  }

  return image;
}

function enhanceImage(image: Matrix<string>, mapping: Record<string, string>) {
  const slice = image.rows % 2 === 0 ? 2 : 3;

  const newSize = image.rows + image.rows / slice;
  const newImage = Matrix.create(newSize, newSize, '');

  for (let rowStep = 0; rowStep < image.rows / slice; rowStep++) {
    for (let colStep = 0; colStep < image.cols / slice; colStep++) {
      const sliceHash = image
        .sliceAsMatrix(
          rowStep * slice,
          rowStep * slice + slice,
          colStep * slice,
          colStep * slice + slice,
        )
        .hash();
      const newHash = mapping[sliceHash].split('/');

      for (let nrow = rowStep * (slice + 1); nrow < (rowStep + 1) * (slice + 1); nrow++) {
        for (let ncol = colStep * (slice + 1); ncol < (colStep + 1) * (slice + 1); ncol++) {
          newImage.set(nrow, ncol, newHash[nrow % (slice + 1)].charAt(ncol % (slice + 1)));
        }
      }
    }
  }

  return newImage;
}
