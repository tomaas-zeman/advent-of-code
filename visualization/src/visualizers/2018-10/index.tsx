import { useEffect, useRef, useState } from 'react';
import { VisualizerProps } from '..';
import * as Plot from '@observablehq/plot';

type Point = {
  position: [number, number];
  velocity: [number, number];
};

type Data = {
  point: Point;
  isTest: boolean;
};

function positionAt(point: Point, time: number): [number, number] {
  return [
    point.position[0] + point.velocity[0] * time,
    point.position[1] + point.velocity[1] * time,
  ];
}

function renderChart(positions: { x: number; y: number }[], container: HTMLDivElement) {
  const plot = Plot.dot(positions, { x: 'x', y: 'y' }).plot();
  container.replaceChildren(plot);
}

export default function Visualizer(props: VisualizerProps) {
  const buffer = useRef(props.buffer as Data[]);
  const chartRef = useRef<HTMLDivElement>(null);
  const time = useRef(0);
  const timeStep = useRef(100);

  const [elapsedTime, setElapsedTime] = useState(0);
  const [runVisualization, setRunVisualization] = useState(false);
  const [done, setDone] = useState(false);

  useEffect(() => {
    if (!runVisualization) {
      return;
    }

    const interval = setInterval(() => {
      const positions = buffer.current.map((data) => {
        const position = positionAt(data.point, time.current);
        return { x: position[0], y: -position[1] };
      });

      const minY = Math.min(...positions.map((p) => p.y));
      const maxY = Math.max(...positions.map((p) => p.y));
      const maxYVelocity = Math.max(
        ...buffer.current.map((data) => Math.abs(data.point.velocity[1])),
      );
      const height = Math.abs(minY - maxY);

      renderChart(positions, chartRef.current!);

      if (maxYVelocity * timeStep.current > height) {
        timeStep.current = 1;
      }
      if (height < (buffer.current[0].isTest ? 9 : 10)) {
        clearInterval(interval);
        setRunVisualization(false);
        setDone(true);
      }

      setElapsedTime(time.current);
      time.current += timeStep.current;
    }, 100);

    return () => clearInterval(interval);
  }, [runVisualization]);

  return (
    <>
      <button
        className="
        rounded-md uppercase py-3 px-6 mb-6
        bg-blue-500 active:bg-blue-600 disabled:bg-green-500"
        onClick={() => setRunVisualization(!runVisualization)}
        disabled={done}
      >
        {!runVisualization && !done && 'Move points!'}
        {(runVisualization || done) && `Elapsed time: ${elapsedTime}`}
      </button>
      <div className="w-full h-[50vh]" ref={chartRef} />
    </>
  );
}
