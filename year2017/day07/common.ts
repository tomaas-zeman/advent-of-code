export type Program = {
  name: string;
  weight: number;
  children: string[];
};

export function parse(data: string[]) {
  const programs: Program[] = [];

  for (const line of data) {
    let children: string[] = [];
    if (line.includes('->')) {
      children = line.split('->')[1].trim().split(', ');
    }
    const [_, name, weight] = line.match(/(\w+) \((\d+)\).*/)!;
    programs.push({ name, weight: parseInt(weight), children });
  }

  return programs;
}

export function findRoot(programs: Program[]) {
  const root = new Set(programs.map((p) => p.name)).difference(
    new Set(programs.flatMap((p) => p.children)),
  );
  return root.values().next().value!;
}
