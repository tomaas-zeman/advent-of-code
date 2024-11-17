import { WebSocketServer } from 'ws';

const PORT = 3333;
let wss: WebSocketServer | null = null;

export async function startWebSocketServer() {
  return new Promise<void>((resolve) => {
    wss = new WebSocketServer({ port: PORT });
    wss.on('connection', () => {
      console.log('Client connected.');
      resolve();
    });
    console.log(`WebSocket server started on port ${PORT}. Waiting for client ...`);
  });
}

export function closeWebSocketServer() {
  wss?.clients.forEach((client) => client.close());
  wss?.close();
}

export function sendData(data: any) {
  if (!wss) {
    throw new Error('WebSocket server is not running!');
  }

  wss.clients.forEach((client) => {
    client.send(JSON.stringify(data));
  });
}
