import { Config } from '../..';
import { parseReports } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const reports = parseReports(data);
  let safeReports = 0;

  for (const report of reports) {
    const diffs = [...report];
    for (let i = 1; i < report.length; i++) {
      diffs[i] = report[i] - report[i - 1];
    }
    if (
      diffs.slice(1).every((v) => v >= 1 && v <= 3) ||
      diffs.slice(1).every((v) => v <= -1 && v >= -3)
    ) {
      safeReports++;
    }
  }

  return safeReports;
}

export const testResult = 2;
