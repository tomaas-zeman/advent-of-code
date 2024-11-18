import { WebSocketServer } from 'ws';

export type Data = { [key: string]: string | number | boolean };

const PORT = 3333;
let wss: WebSocketServer | null = null;
let metadata: Data = {};

export async function startWebSocketServer() {
  return new Promise<(data: Data) => void>((resolve) => {
    wss = new WebSocketServer({ port: PORT });
    wss.on('connection', () => {
      console.log('Client connected.');
      resolve(setRequestMetadata);
    });
    console.log(`WebSocket server started on port ${PORT}. Waiting for client ...`);
  });
}

export function closeWebSocketServer() {
  wss?.clients.forEach((client) => client.close());
  wss?.close();
}

export function setRequestMetadata(data: Data) {
  metadata = data;
}

export function visualize(data: Data) {
  // WSS is not running, we intentionally ignore it.
  // This allows to have code that calls this all the time
  // but runs visualizations if we enable it.
  if (!wss) {
    return;
  }

  wss.clients.forEach((client) => {
    client.send(JSON.stringify({ ...metadata, ...data }));
  });
}
