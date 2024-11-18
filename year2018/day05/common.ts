import { visualize as sendData } from '../../ts-runner/wsserver';

function visualize(data: any, isTest?: boolean) {
  if (!isTest) {
    return;
  }
  sendData(data);
}

export function collapsePolymer(initialPolymer: string, isTest?: boolean) {
  const polymer = initialPolymer.split('');
  visualize({ start: true }, isTest);

  for (let i = 0; i < polymer.length - 1; i++) {
    visualize({ polymer: polymer.join(''), index: i }, isTest);
    const l = polymer[i];
    const r = polymer[i + 1];

    if (l !== r && l.toLowerCase() === r.toLowerCase()) {
      visualize({ index: i, nextIndex: Math.max(-1, i - 2) }, isTest);
      polymer.splice(i, 2);
      i = Math.max(-1, i - 2);
    }
  }

  visualize({ stop: true }, isTest);

  return polymer.length;
}
