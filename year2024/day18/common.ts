import { Config } from '../..';

export function parse(data: string[], config: Config): [[number, number][], [number, number]] {
  const bytes = data.map((line) => line.split(',').asInt()) as [number, number][];
  const size: [number, number] = config.isTest ? [7, 7] : [71, 71];
  return [bytes, size];
}
