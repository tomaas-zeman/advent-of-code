import { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';

function App() {
  const [data, setData] = useState('');

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:3333');
    ws.addEventListener('message', (event) => {
      setData(JSON.parse(event.data));
    });
    return () => ws.close();
  }, []);

  return (
    <>
      <div>Hello World!</div>
      <div>Here is some data: {JSON.stringify(data)}</div>
    </>
  );
}

createRoot(document.getElementById('root')!).render(<App />);
