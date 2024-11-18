import { useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { NoVisualization, Visualizer, visualizers } from './visualizers';
import './index.css';

enum State {
  IDLE = 'idle',
  LOADING_DATA = 'loading data ...',
  DATA_LOADED = 'data loaded',
}

function App() {
  const buffer = useRef<string[]>([]);
  const visualizer = useRef<Visualizer>(NoVisualization);
  const [state, setState] = useState<State>(State.IDLE);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:3333');
    ws.addEventListener('message', (event) => {
      const data = JSON.parse(event.data);
      if (data.start) {
        buffer.current = [];
        visualizer.current = visualizers[data.year][data.day];
        setState(State.LOADING_DATA);
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
    <>
      <div>Client state: {state}</div>
      {state === State.DATA_LOADED && <Visualizer buffer={buffer.current} />}
    </>
  );
}

createRoot(document.getElementById('root')!).render(<App />);
