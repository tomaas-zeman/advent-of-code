import { Config } from "../..";
import { computeComplexitiesNumerical } from "./common";

export async function run(data: string[], config: Config): Promise<string | number> {
  return computeComplexitiesNumerical(data, 25);
}

export const testResult = 154115708116294;
