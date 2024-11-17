import { createRoot } from 'react-dom/client';
import './index.css';

function App() {
  return <div>Hello World!</div>;
}

createRoot(document.getElementById('root')!).render(<App />);
