import countBy from 'lodash/countBy';
import { Dictionary } from 'lodash';
import { Config } from '../..';
import { sum } from '../../aocutils';
import { findRoot, parse, Program } from './common';

function itemWeight(item: Dictionary<number>, condition: (v: number) => boolean) {
  return parseInt(Object.entries(item).filter(([_, v]) => condition(v))[0][0]);
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const programs = parse(data);
  const programsByName = Object.fromEntries(programs.map((p) => [p.name, p]));
  let result: number | null = null;

  function browseTree(root: Program) {
    if (!root.children.length) {
      return root.weight;
    }

    const childWeights: number[] = [];
    for (const child of root.children) {
      childWeights.push(browseTree(programsByName[child]));
    }

    const weightOccurences = countBy(childWeights);
    if (Object.keys(weightOccurences).length !== 1) {
      const wrongItemWeight = itemWeight(weightOccurences, (count) => count === 1);
      const correctItemWeight = itemWeight(weightOccurences, (count) => count !== 1);
      const wrongProgramName = root.children[childWeights.indexOf(wrongItemWeight)];
      if (!result) {
        result = programsByName[wrongProgramName].weight + (correctItemWeight - wrongItemWeight);
      }
    }

    return root.weight + sum(childWeights);
  }

  browseTree(programsByName[findRoot(programs)]);

  return result!;
}

export const testResult = 60;
