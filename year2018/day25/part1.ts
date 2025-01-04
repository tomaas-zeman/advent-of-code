import { Config } from '../..';
import { manhattan } from '../../aocutils';
import { parse, Point } from './common';

function findNearConstellations(constellations: Point[][], star: Point) {
  const nearConsteallations: number[] = [];
  for (let i = 0; i < constellations.length; i++) {
    for (let j = 0; j < constellations[i].length; j++) {
      if (manhattan(star, constellations[i][j]) <= 3) {
        nearConsteallations.push(i);
      }
    }
  }
  return nearConsteallations;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const stars = parse(data);
  let constellations: Point[][] = [];

  for (let star of stars) {
    const nearConstellations = findNearConstellations(constellations, star);

    if (nearConstellations.length === 0) {
      constellations.push([star]);
    } else {
      if (nearConstellations.length === 1) {
        constellations[nearConstellations[0]].push(star);
      } else {
        // There's a chance we have multiple constellations at the same distance.
        // That means that our new star connects them together
        let newConstellation: Point[] = [star];
        for (let nearConstellation of nearConstellations) {
          newConstellation = [...newConstellation, ...constellations[nearConstellation]];
          constellations[nearConstellation] = []; // clear it, we'll filter it out later
        }
        constellations = [...constellations.filter((c) => c.length > 0), newConstellation];
      }
    }
  }

  return constellations.length;
}

export const testResult = 8;
