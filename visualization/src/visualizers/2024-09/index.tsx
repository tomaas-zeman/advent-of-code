import { createRef, RefObject, useEffect, useRef } from 'react';
import { VisualizerProps } from '..';
import range from 'lodash/range';

type Config = {
  fs: (number | null)[];
};

type Shift = { length: number; source: number; destination: number };

function createGridRefs(items: number) {
  const gridRefs: RefObject<HTMLDivElement>[] = [];
  for (let i = 0; i < items; i++) {
    gridRefs.push(createRef<HTMLDivElement>());
  }
  return gridRefs;
}

function renderGrid(length: number, gridRefs: RefObject<HTMLDivElement>[]) {
  return (
    <div className={`grid grid-cols-450 gap-[2px]`}>
      {range(0, length).map((i) => (
        <div
          ref={gridRefs[i]}
          className="
            flex
            w-[4px] h-[4px] 
            place-content-center"
        />
      ))}
    </div>
  );
}

export default function Visualizer(props: VisualizerProps) {
  const { fs } = useRef(props.buffer[0] as Config).current;
  const shifts = useRef(props.buffer.slice(1) as Shift[]).current;
  const gridRefs = useRef(createGridRefs(fs.length));

  const changeColor = (index: number, color: string) => {
    const el = gridRefs.current[index].current;
    el?.classList.replace('bg-gray-500', color);
    el?.classList.replace('bg-red-300', color);
  };

  useEffect(() => {
    fs.forEach((value, index) => {
      if (value == null) {
        gridRefs.current[index].current?.classList.add('bg-gray-500');
      } else {
        gridRefs.current[index].current?.classList.add('bg-red-300');
      }
    });
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      const shift = shifts.shift();
      if (!shift || !props.runVisualization) {
        clearInterval(interval);
        props.onVisualizationEnd();
        return;
      }
      for (let index = shift.source; index <= shift.source + shift.length; index++) {
        changeColor(index, 'bg-gray-500');
      }
      for (let index = shift.destination; index < shift.destination + shift.length; index++) {
        changeColor(index, 'bg-green-300');
      }
    });

    return () => clearInterval(interval);
  }, [props.runVisualization]);

  return renderGrid(fs.length, gridRefs.current);
}
