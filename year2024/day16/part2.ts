import { Config } from '../..';
import { dijkstra, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [maze, start, end] = parse(data);
  const distancesFromStart = dijkstra(maze.clone(), start);
  const distancesFromEnd = dijkstra(maze.clone(), end);

  const shortestDistance = distancesFromStart.get(end);
  return [...maze.findAll('.'), start, end].filter((node) => {
    const fromStart = distancesFromStart.get(node);
    const fromEnd = distancesFromEnd.get(node);
    return (
      fromStart + fromEnd === shortestDistance || fromStart + fromEnd - 1000 === shortestDistance
    );
  }).length;
}

export const testResult = 45;
