import Visualizer_2018_05 from './2018-05';
import Visualizer_2018_10 from './2018-10';
import Visualizer_2024_01 from './2024-01';
import Visualizer_2024_08 from './2024-08';

export type VisualizerProps = {
  buffer: any[];
  runVisualization: boolean;
  onVisualizationEnd: Function;
};

export type Visualizer = React.FunctionComponent<VisualizerProps>;

export const visualizers: { [year: string]: { [day: string]: Visualizer } } = {
  '2018': {
    '05': Visualizer_2018_05,
    '10': Visualizer_2018_10,
  },
  '2024': {
    '01': Visualizer_2024_01,
    '08': Visualizer_2024_08,
  },
};

export function NoVisualization() {
  return null;
}
