export function parseReports(data: string[]) {
  return data.map((line) => line.split(' ').map((value) => parseInt(value)));
}
