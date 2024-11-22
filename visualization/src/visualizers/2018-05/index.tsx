import { useEffect, useRef, useState } from 'react';
import { VisualizerProps } from '..';

type Data = {
  polymer: string;
  index: number;
};

export default function Visualizer(props: VisualizerProps) {
  const buffer = useRef(props.buffer as Data[]);

  const [runVisualization, setRunVisualization] = useState(false);
  const [polymer, setPolymer] = useState('');
  const [index, setIndex] = useState(0);

  useEffect(() => {
    if (!runVisualization) {
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
    }, 200);

    return () => clearInterval(interval);
  }, [runVisualization]);

  return (
    <>
      <button
        className="rounded-md bg-blue-500 py-3 px-6 uppercase mb-6 active:bg-blue-600"
        onClick={() => setRunVisualization(true)}
      >
        Reduce polymer!
      </button>
      <div className="relative tracking-[0.5rem] font-mono text-xl">
        {polymer}
        <div
          className="
          absolute inset-0 
          transition ease-in-out duration-300 
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
