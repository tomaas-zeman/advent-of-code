import { Config } from '../..';
import { initTick, parseInput } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [tracks, carts] = parseInput(data);

  while (true) {
    const [orderedCarts, cartPositions] = initTick(carts);

    for (let cart of orderedCarts) {
      cartPositions.delete(cart.positionAsString());

      // Move and detect collision
      const [row, col] = cart.move(tracks);
      if (cartPositions.has(cart.positionAsString())) {
        return cart.positionAsString();
      }

      cartPositions.add(cart.positionAsString());
    }
  }
}

export const testResult = '7,3';
