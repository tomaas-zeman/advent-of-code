import { DefaultMap } from '../../aocutils';

type Layer = { range: number; scanner: number; direction: 'up' | 'down' };

export function parse(data: string[]): [DefaultMap<number, Layer>, number] {
  const firewall = new DefaultMap<number, Layer>(() => ({
    range: 0,
    scanner: -1,
    direction: 'down',
  }));

  for (const line of data) {
    const [depth, range] = line.split(': ').asInt();
    firewall.set(depth, { range, scanner: 0, direction: 'down' });
  }

  const numberOfLayers = Math.max(...firewall.keys());

  return [firewall, numberOfLayers];
}
