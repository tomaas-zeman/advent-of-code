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
  const buffer = useRef<string[]>([]);
  const visualizer = useRef<Visualizer>(NoVisualization);
  const [state, setState] = useState<State>(State.IDLE);
  const [date, setDate] = useState<string>('');

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
        buffer.current.push(event.data);
      }
    });
    return () => ws.close();
  }, []);

  const Visualizer = visualizer.current;

  return (
    <div className="container m-20">
      <h1 className="text-5xl mb-6">Advent of Code Visualization</h1>
      <h2 className="text-xl italic mb-6">{date}</h2>
      <hr className="mb-6" />
      {state === State.DATA_LOADED && <Visualizer buffer={buffer.current} />}
      {state !== State.DATA_LOADED && (
        <div className="text-xl">Waiting for visualization data ...</div>
      )}
    </div>
  );
}

createRoot(document.getElementById('root')!).render(<App />);
