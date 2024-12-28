export function parse(data: string[]) {
  return data.map((line) => line.split(/\s/).asInt());
}
