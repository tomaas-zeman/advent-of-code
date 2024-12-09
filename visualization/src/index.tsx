import { useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { NoVisualization, Visualizer, visualizers } from './visualizers';
import './index.css';

enum State {
  IDLE,
  LOADING_DATA,
  DATA_LOADED,
}

function App() {
  const buffer = useRef<any[]>([]);
  const visualizer = useRef<Visualizer>(NoVisualization);
  const [state, setState] = useState<State>(State.IDLE);
  const [date, setDate] = useState<string>('');
  const [bufferSize, setBufferSize] = useState(0);
  const [runVisualization, setRunVisualization] = useState(false);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:3333');
    ws.addEventListener('message', (event) => {
      const data = JSON.parse(event.data);
      if (data.start) {
        buffer.current = [];
        visualizer.current = visualizers[data.year][data.day];
        setState(State.LOADING_DATA);
        setDate(`${data.year} / ${data.day}`);
      } else if (data.stop) {
        setState(State.DATA_LOADED);
      } else {
        buffer.current.push(data);
        setBufferSize(buffer.current.length);
      }
    });
    return () => ws.close();
  }, []);

  // For demo purposes
  // useEffect(() => {
  //   visualizer.current = visualizers['2024']['08'];
  //   buffer.current.push({
  //     areaSize: [12, 12],
  //     antennas: {
  //       A: [
  //         [3, 5],
  //         [8, 9],
  //         [10, 10],
  //       ],
  //     },
  //   });
  //   buffer.current.push({ antinode: [1, 2] });
  //   setBufferSize(buffer.current.length);
  //   setState(State.DATA_LOADED);
  // }, []);

  const Visualizer = visualizer.current;

  return (
    <div className="container m-20">
      <div className="flex">
        <div>
          <h1 className="text-5xl mb-6">Advent of Code Visualization</h1>
          <h2 className="text-xl italic mb-6">{date}</h2>
        </div>
        <button
          className="rounded-md bg-blue-500 py-3 px-6 uppercase mb-6 active:bg-blue-600 ml-10 h-min"
          onClick={() => setRunVisualization(!runVisualization)}
        >
          Toggle visualization
        </button>
      </div>
      <hr className="mb-6" />
      {state === State.DATA_LOADED && (
        <Visualizer
          buffer={buffer.current}
          runVisualization={runVisualization}
          onVisualizationEnd={() => setRunVisualization(false)}
        />
      )}
      {state !== State.DATA_LOADED && (
        <div className="text-xl">Waiting for visualization data ... buffer size: {bufferSize}</div>
      )}
    </div>
  );
}

createRoot(document.getElementById('root')!).render(<App />);
