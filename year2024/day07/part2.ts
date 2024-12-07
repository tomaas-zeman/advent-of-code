import { Config } from '../..';
import { computeCalibrationResult, OperatorsPart2 } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return computeCalibrationResult(data, OperatorsPart2);
}

export const testResult = 11387;
