import { useEffect, useRef, useState } from 'react';
import { VisualizerProps } from '..';

type Data = {
  polymer: string;
  index: number;
};

export default function Visualizer(props: VisualizerProps) {
  const buffer = useRef(props.buffer as Data[]);
  const [polymer, setPolymer] = useState('');
  const [index, setIndex] = useState(0);

  useEffect(() => {
    if (!props.runVisualization) {
      const item = buffer.current.shift();
      if (!item) {
        return;
      }
      setPolymer(item.polymer);
      setIndex(item.index);
      return;
    }

    const interval = setInterval(() => {
      const item = buffer.current.shift();
      if (!item) {
        clearInterval(interval);
        return;
      }

      setPolymer(item.polymer);
      setIndex(item.index);
    }, 500);

    return () => clearInterval(interval);
  }, [props.runVisualization]);

  return (
    <>
      <div className="relative tracking-[0.5rem] font-mono text-xl">
        {polymer}
        <div
          className="
          absolute inset-0 
          transition ease-in-out duration-[400] 
          border-solid border-4 border-green-200 rounded-md 
          w-[3.5rem] h-10 
          -left-[0.8rem] -top-[0.4rem] 
          opacity-50"
          style={{ transform: `translateX(${1.26 * index}rem)` }}
        />
      </div>
    </>
  );
}
