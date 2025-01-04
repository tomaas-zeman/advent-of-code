import { Config } from '../..';
import { manhattan, mergePoints } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const particles = parse(data);
  const distances = new Map<number, number>();

  for (let tick = 0; tick < 1000; tick++) {
    for (let i = 0; i < particles.length; i++) {
      const particle = particles[i];
      particle.velocity = mergePoints(particle.velocity, particle.acceleration);
      particle.position = mergePoints(particle.position, particle.velocity);
      distances.set(i, manhattan([0, 0, 0], particle.position));
    }
  }

  const smallestDistance = Math.min(...distances.values());
  for (let particle = 0; particle < particles.length; particle++) {
    if (distances.get(particle) === smallestDistance) {
      return particle;
    }
  }

  throw new Error('Should not happen!');
}

export const testResult = 0;
