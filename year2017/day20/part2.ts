import groupBy from 'lodash/groupBy';
import { Config } from '../..';
import { mergePoints } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  let particles = parse(data);

  for (let tick = 0; tick < 1000; tick++) {
    for (let i = 0; i < particles.length; i++) {
      const particle = particles[i];
      particle.velocity = mergePoints(particle.velocity, particle.acceleration);
      particle.position = mergePoints(particle.position, particle.velocity);
    }

    const collisions = groupBy(particles, (p) => p.position.join(''));
    for (const collision of Object.values(collisions)) {
      if (collision.length === 1) {
        continue;
      }

      particles = particles.filter(p => !collision.map(p => p.id).includes(p.id));
    }
  }

  return particles.length;
}

export const testResult = 1;
