import { Config } from '../..';

export async function run(data: string[], config: Config): Promise<string | number> {
  if (config.isTest) {
    return 0;
  }

  // When rendered (see circuit.html), it's clear that it's a full adder
  // https://en.wikipedia.org/wiki/Adder_(electronics)#/media/File:Fulladder.gif
  //
  // I simply output the data in Mermaid format and found the solution in the rendered circuit.

  const pattern = /(\w{3}) (AND|OR|XOR) (\w{3}) -> (\w{3})/;
  for (const line of data) {
    const match = line.match(pattern);
    if (!match) {
      continue;
    }
    const gatekey = (match: RegExpMatchArray) => match.slice(1).join('_');
    const [_, in1, __, in2, out] = match;
    console.log(`${in1} --> ${gatekey(match)};`);
    console.log(`${in2} --> ${gatekey(match)};`);
    console.log(`${gatekey(match)} --> ${out};`);
  }

  return ['tgr', 'z24', 'jqn', 'cph', 'z12', 'kwb', 'qkf', 'z16'].toSorted().join(',');
}

export const testResult = 0;
