import { Config } from '../..';
import { parseReports } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const reports = parseReports(data);
  let safeReports = 0;

  for (const report of reports) {
    for (let removedLevel = 0; removedLevel < report.length; removedLevel++) {
      const newReport = [...report];
      newReport.splice(removedLevel, 1);

      const diffs = [...newReport];
      for (let i = 1; i < newReport.length; i++) {
        diffs[i] = newReport[i] - newReport[i - 1];
      }
      if (
        diffs.slice(1).every((v) => v >= 1 && v <= 3) ||
        diffs.slice(1).every((v) => v <= -1 && v >= -3)
      ) {
        safeReports++;
        break;
      }
    }
  }

  return safeReports;
}

export const testResult = 4;
