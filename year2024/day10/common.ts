import { Matrix } from '../../aocutils';

export type Point = [number, number];

function parse(data: string[]): [Matrix<number>, Point[]] {
  const map = new Matrix(data.map((row) => row.split('').asInt()));
  const trailheads = map.searchAll(0);
  return [map, trailheads];
}

function calculateScores(completePaths: Point[][], pathHash: (path: Point[]) => string) {
  const scores = completePaths.reduce(
    (acc, path) => {
      const trailheadHash = path[0].join(':');
      if (!acc[trailheadHash]) {
        acc[trailheadHash] = new Set();
      }
      acc[trailheadHash].add(pathHash(path));
      return acc;
    },
    {} as { [trailhead: string]: Set<string> },
  );

  return Object.values(scores).reduce((sum, score) => sum + score.size, 0);
}

export function calculateTrailheadRatings(data: string[], hash: (path: Point[]) => string): number {
  const [map, trailheads] = parse(data);

  const completePaths: Point[][] = [];
  const pathsInProgress = trailheads.reduce((paths, trailhead) => {
    paths.push([trailhead]);
    return paths;
  }, [] as Point[][]);

  while (pathsInProgress.length > 0) {
    const path = pathsInProgress.pop()!;
    const currentPosition = path.get(-1);
    const currentSlope = map.get(...currentPosition);
    const nextPositions = map.neighborPositions(...currentPosition, false);

    for (const nextPosition of nextPositions) {
      const slope = map.get(...nextPosition);
      if (currentSlope + 1 === slope) {
        (slope === 9 ? completePaths : pathsInProgress).push([...path, nextPosition]);
      }
    }
  }

  return calculateScores(completePaths, hash);
}
