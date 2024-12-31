export function getResult(data: string[], offsetChange: (offset: number) => number) {
  const jumps = data.asInt();

  let steps = 0;
  let ip = 0;
  while (ip < jumps.length) {
    const offset = jumps[ip];
    jumps[ip] += offsetChange(offset);
    ip += offset;
    steps++;
  }

  return steps;
}
