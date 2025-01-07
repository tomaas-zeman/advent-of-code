import { Config } from "../..";
import { computeComplexities } from "./common";

export async function run(data: string[], config: Config): Promise<string | number> {
  return computeComplexities(data, 2);
}

export const testResult = 126384;
