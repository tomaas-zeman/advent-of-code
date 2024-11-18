import { Config } from "../..";

export async function run(data: string[], config: Config): Promise<string | number> {
  return data.reduce((acc, value) => acc + parseInt(value), 0);
}

export const testResult = 3;
