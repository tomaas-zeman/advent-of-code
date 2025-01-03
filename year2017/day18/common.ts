import { DefaultMap } from '../../aocutils';

export type Instruction = 'jgz' | 'snd' | 'rcv' | 'set' | 'add' | 'mul' | 'mod';
export type Command = [Instruction, string, string];

export class MessageBus {
  private clients: number[] = [];
  private messages = new DefaultMap<number, number[]>(() => []);
  private internal: boolean;

  constructor(internal: boolean) {
    this.internal = internal;
  }

  registerClient(computer: Computer) {
    this.clients.push(computer.id);
  }

  sendMessage(senderId: number, message: number) {
    if (this.internal) {
      this.messages.get(senderId).push(message);
      return;
    }
    for (const id of this.clients) {
      if (senderId !== id) {
        this.messages.get(id).push(message);
      }
    }
  }

  getOldestMessage(receiverId: number) {
    return this.messages.get(receiverId).shift();
  }

  getNewestMessage(receiverId: number) {
    return this.messages.get(receiverId).pop();
  }
}

export class Computer {
  id: number;
  ip = 0;
  sentMessages = 0;
  waitingForMessage = false;

  private registers: DefaultMap<string, number>;
  private bus: MessageBus;
  private instructions = {
    jgz: (register: string, value: string) => {
      this.ip += this.getValue(register) > 0 ? this.getValue(value) : 1;
    },
    snd: (register: string) => {
      this.bus.sendMessage(this.id, this.getValue(register));
      this.ip++;
      this.sentMessages++;
    },
    rcv: (register: string) => {
      const message = this.bus.getOldestMessage(this.id);
      if (message) {
        this.registers.set(register, message);
        this.ip++;
        this.waitingForMessage = false;
      } else {
        this.waitingForMessage = true;
      }
    },
    set: (register: string, value: string) => {
      this.registers.set(register, this.getValue(value));
      this.ip++;
    },
    add: (register: string, value: string) => {
      this.registers.mapItem(register, (v) => v + this.getValue(value));
      this.ip++;
    },
    mul: (register: string, value: string) => {
      this.registers.mapItem(register, (v) => v * this.getValue(value));
      this.ip++;
    },
    mod: (register: string, value: string) => {
      this.registers.mapItem(register, (v) => v % this.getValue(value));
      this.ip++;
    },
  };

  constructor(id: number, registers: DefaultMap<string, number>, bus: MessageBus) {
    this.id = id;
    this.registers = registers;
    this.bus = bus;
    this.bus.registerClient(this);
  }

  processInstruction(instruction: Instruction, register: string, value: string) {
    this.instructions[instruction](register, value);
  }

  private getValue(registerOrValue: string) {
    if (registerOrValue.match(/\d+/)) {
      return parseInt(registerOrValue);
    }
    return this.registers.get(registerOrValue);
  }
}
