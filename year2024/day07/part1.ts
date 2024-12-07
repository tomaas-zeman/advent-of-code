import { Config } from '../..';
import { computeCalibrationResult, OperatorsPart1 } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return computeCalibrationResult(data, OperatorsPart1);
}

export const testResult = 3749;
