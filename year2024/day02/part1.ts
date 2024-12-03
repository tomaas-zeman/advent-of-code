import { Config } from '../..';
import { isSafe, parseReports } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const reports = parseReports(data);
  return reports.filter(isSafe).length;
}

export const testResult = 2;
