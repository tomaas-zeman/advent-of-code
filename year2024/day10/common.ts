import { DefaultMap, Matrix } from '../../aocutils';

export type Point = [number, number];

function parse(data: string[]): [Matrix<number>, Point[]] {
  const map = new Matrix(data.map((row) => row.split('').asInt()));
  const trailheads = map.searchAll(0);
  return [map, trailheads];
}

function calculateScores(completePaths: Point[][], pathHash: (path: Point[]) => string) {
  const scores = new DefaultMap<string, Set<string>>(() => new Set());

  for (const path of completePaths) {
    const trailheadHash = path[0].join(':');
    scores.get(trailheadHash).add(pathHash(path));
  }

  return scores.values().reduce((sum, score) => sum + score.size, 0);
}

function findAllPaths(map: Matrix<number>, trailheads: Point[]) {
  const completePaths: Point[][] = [];
  const pathsInProgress = trailheads.map((trailhead) => [trailhead]);

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

  return completePaths;
}

export function calculateTrailheadRatings(data: string[], hash: (path: Point[]) => string): number {
  const [map, trailheads] = parse(data);
  const paths = findAllPaths(map, trailheads);
  return calculateScores(paths, hash);
}
