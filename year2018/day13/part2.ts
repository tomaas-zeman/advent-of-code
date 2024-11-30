import { Config } from '../..';
import { initTick, parseInput } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  let [tracks, carts] = parseInput(data);

  while (true) {
    if (carts.length === 1) {
      return carts[0].positionAsString();
    }

    const [orderedCarts, cartPositions] = initTick(carts);

    for (let cart of orderedCarts) {
      cartPositions.delete(cart.positionAsString());

      // Move, detect collision and remove colliding carts
      const [row, col] = cart.move(tracks);
      if (cartPositions.has(cart.positionAsString())) {
        carts = carts.filter((c) => c.positionAsString() !== cart.positionAsString());
      }

      cartPositions.add(cart.positionAsString());
    }
  }
}

export const testResult = '6,4';
