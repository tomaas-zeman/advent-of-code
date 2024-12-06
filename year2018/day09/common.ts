class Marble {
  id: number;
  next: Marble;
  prev: Marble;

  constructor(id: number) {
    this.id = id;
  }

  left(steps: number) {
    let marble: Marble = this;
    for (let i = 0; i < steps; i++) {
      marble = marble.prev;
    }
    return marble;
  }
}

class Scores {
  scores: { [player: number]: number } = {};

  add(player: number, score: number) {
    if (!this.scores[player]) {
      this.scores[player] = 0;
    }
    this.scores[player] += score;
  }
}

export function computeScores(players: number, marbles: number) {
  const scores = new Scores();

  let currentMarble = new Marble(0);
  currentMarble.next = currentMarble;
  currentMarble.prev = currentMarble;

  let currentPlayer = 1;

  for (let newMarbleId = 1; newMarbleId <= marbles; newMarbleId++) {
    if (newMarbleId % 23 === 0) {
      const marbleToRemove = currentMarble.left(7);
      scores.add(currentPlayer, newMarbleId);
      scores.add(currentPlayer, marbleToRemove.id);

      marbleToRemove.prev.next = marbleToRemove.next;
      marbleToRemove.next.prev = marbleToRemove.prev;

      currentMarble = marbleToRemove.next;
    } else {
      const newMarble = new Marble(newMarbleId);
      const firstMarble = currentMarble.next;
      const secondMarble = firstMarble.next;

      firstMarble.next = newMarble;
      secondMarble.prev = newMarble;
      newMarble.prev = firstMarble;
      newMarble.next = secondMarble;

      currentMarble = newMarble;
    }

    currentPlayer = (currentPlayer + 1) % players;
  }

  return Math.max(...Object.values(scores.scores));
}

export function parseData(data: string[]): [number, number] {
  const [_, players, marbles] = data[0].match(/(\d+) players.*worth (\d+) points/)?.asInt()!;
  return [players, marbles];
}
