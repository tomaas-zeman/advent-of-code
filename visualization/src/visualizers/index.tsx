import Visualizer_2018_05 from './2018-05';

export type VisualizerProps = {
  buffer: string[];
};

export type Visualizer = React.FunctionComponent<VisualizerProps>;

export const visualizers: { [year: string]: { [day: string]: Visualizer } } = {
  '2018': {
    '05': Visualizer_2018_05,
  },
};

export function NoVisualization() {
  return null;
}
