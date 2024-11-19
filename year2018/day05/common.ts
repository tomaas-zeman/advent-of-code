import { Config } from '../..';

export async function collapsePolymer(initialPolymer: string, config: Config) {
  const { visualization, isTest } = config;
  if (!isTest) {
    visualization.skip();
  }

  const polymer = initialPolymer.split('');
  await visualization.start();

  for (let i = 0; i < polymer.length - 1; i++) {
    visualization.sendData(() => ({ polymer: polymer.join(''), index: i }));
    const l = polymer[i];
    const r = polymer[i + 1];

    if (l !== r && l.toLowerCase() === r.toLowerCase()) {
      visualization.sendData({ index: i, nextIndex: Math.max(-1, i - 2) });
      polymer.splice(i, 2);
      i = Math.max(-1, i - 2);
    }
  }

  visualization.stop();

  return polymer.length;
}
