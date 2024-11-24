const RULE_WIDTH = 5;

export type Rule = {
  pattern: string;
  result: string;
};

export function parse(data: string[]) {
  const state = data[0].split(' ')[2];
  const rules: Rule[] = data.slice(2).map((line) => {
    const [pattern, result] = line.split(' => ');
    return { pattern, result };
  });
  return { state, rules };
}

function pad(size: number) {
  return new Array(RULE_WIDTH - Math.min(5, size)).fill('.').join('');
}

function leftPad(state: string) {
  return pad(state.match(/^(\.*)/)![1].length);
}

function rightPad(state: string) {
  return pad(state.match(/(\.*)$/)![1].length);
}

function sumOfPotsWithPlants(state: string, leftPadSize: number) {
  return state
    .split('')
    .reduce((sum, pot, index) => sum + (pot === '#' ? index - leftPadSize : 0), 0);
}

function trim(state: string) {
  return state.slice(state.indexOf('#'), state.lastIndexOf('#') + 1);
}

export function computeSumOfPotsWithPlants(data: string[], generations: number) {
  const { state, rules } = parse(data);

  const oldGenerations = new Set();
  let leftPadSize = 0;
  let prevState = state;

  for (let generation = 0; generation < generations; generation++) {
    leftPadSize += leftPad(prevState).length;
    prevState = `${leftPad(prevState)}${prevState}${rightPad(prevState)}`;
    let nextState = prevState;

    for (let i = 0; i < nextState.length - RULE_WIDTH; i++) {
      const slice = prevState.slice(i, i + RULE_WIDTH);
      let matchFound = false;
      for (let rule of rules) {
        if (slice === rule.pattern) {
          nextState = `${nextState.slice(0, i + 2)}${rule.result}${nextState.slice(i + 3)}`;
          matchFound = true;
          break;
        }
      }

      if (!matchFound) {
        nextState = `${nextState.slice(0, i + 2)}.${nextState.slice(i + 3)}`;
      }
    }

    prevState = nextState;

    const trimmedState = trim(prevState);
    if (oldGenerations.has(trimmedState)) {
      const remainingGens = generations - generation - 1;
      const potsWithPlants = prevState.replaceAll('.', '').length;
      return remainingGens * potsWithPlants + sumOfPotsWithPlants(prevState, leftPadSize);
    } else {
      oldGenerations.add(trimmedState);
    }
  }

  return sumOfPotsWithPlants(prevState, leftPadSize);
}
