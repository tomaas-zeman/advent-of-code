import { WebSocketServer } from 'ws';
import { Config } from '..';

export type Data = { [key: string]: string | number | boolean };

export class NoVisualization {
  setRequestMetadata(metadata: Data) {}
  sendData(data: Data | (() => Data)) {}
  start(): Promise<void> {
    return Promise.resolve();
  }
  stop() {}
  skip() {}
}

export class Visualization {
  private wsPort = 3333;
  private config: Config;
  private skipped: boolean = false;

  private wss: WebSocketServer | null = null;

  constructor(config: Config) {
    this.config = config;
  }

  private startWebSocketServer() {
    return new Promise<void>((resolve) => {
      this.wss = new WebSocketServer({ port: this.wsPort });
      this.wss.on('connection', () => {
        console.log('Client connected.');
        resolve();
      });
      console.log(`WebSocket server started on port ${this.wsPort}. Waiting for client ...`);
    });
  }

  private stopWebSocketServer() {
    this.wss?.clients.forEach((client) => client.close());
    this.wss?.close();
    console.log('Client disconnected.');
  }

  sendData(data: Data | (() => Data)) {
    if (this.skipped) {
      return;
    }
    this.wss?.clients.forEach((client) => {
      const payload = { ...this.config, ...(typeof data === 'function' ? data() : data) };
      // @ts-ignore
      delete payload.visualization;
      client.send(JSON.stringify(payload));
    });
  }

  async start(): Promise<void> {
    if (this.skipped) {
      return;
    }
    await this.startWebSocketServer();
    this.sendData({ start: true });
  }

  stop() {
    if (this.skipped) {
      return;
    }
    this.sendData({ stop: true });
    this.stopWebSocketServer();
  }

  skip() {
    this.skipped = true;
  }
}
