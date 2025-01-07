import { Config } from "../..";
import { computeComplexities } from "./common";

export async function run(data: string[], config: Config): Promise<string | number> {
  return computeComplexities(data, 25);
}

export const testResult = 154115708116294;
