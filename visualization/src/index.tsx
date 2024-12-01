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
  //   visualizer.current = visualizers['2024']['01'];
  //   buffer.current.push({
  //     counts: {3: 3, 4: 1, 5: 1, 9: 1},
  //     numbers: [3, 4, 2, 1, 3, 3]
  //   })
  //   setBufferSize(buffer.current.length);
  //   setState(State.DATA_LOADED);
  // }, []);

  const Visualizer = visualizer.current;

  return (
    <div className="container m-20">
      <h1 className="text-5xl mb-6">Advent of Code Visualization</h1>
      <h2 className="text-xl italic mb-6">{date}</h2>
      <hr className="mb-6" />
      {state === State.DATA_LOADED && <Visualizer buffer={buffer.current} />}
      {state !== State.DATA_LOADED && (
        <div className="text-xl">Waiting for visualization data ... buffer size: {bufferSize}</div>
      )}
    </div>
  );
}

createRoot(document.getElementById('root')!).render(<App />);
