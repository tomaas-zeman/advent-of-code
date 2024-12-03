import { Config } from '../..';
import { isSafe, parseReports } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const reports = parseReports(data);
  return reports.filter((report) => {
    for (let removedLevel = 0; removedLevel < report.length; removedLevel++) {
      const newReport = [...report];
      newReport.splice(removedLevel, 1);
      if (isSafe(newReport)) {
        return true;
      }
    }
    return false;
  }).length;
}

export const testResult = 4;
