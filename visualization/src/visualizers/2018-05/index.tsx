import { VisualizerProps } from '..';

export default function Visualizer(props: VisualizerProps) {
  return (
    <>
      <div>Visualizer 2018/5</div>
      {(props.buffer || []).map((item) => (
        <div>{item}</div>
      ))}
    </>
  );
}
