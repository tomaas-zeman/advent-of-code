enum EventType {
  ShiftStart,
  FallAsleep,
  WakeUp,
}

type Event = {
  time: Date;
  type: EventType;
};

export class Guard {
  id: number;
  events: Event[];
  private _sleepingHistogram: number[] | undefined;
  private _totalSleepTime: number | undefined;

  constructor(id: number) {
    this.id = id;
    this.events = [];
  }

  get sleepingHistogram() {
    if (!this._sleepingHistogram) {
      this._sleepingHistogram = this.createSleepingHistogram();
    }
    return this._sleepingHistogram;
  }

  get totalSleepTime() {
    if (!this._totalSleepTime) {
      this._totalSleepTime = this.calculateTotalSleepTime();
    }
    return this._totalSleepTime;
  }

  getMaxOverlap() {
    return Math.max(...this.sleepingHistogram);
  }

  getMinuteOfMaxOverlap() {
    return this.sleepingHistogram.findIndex((value) => value === this.getMaxOverlap());
  }

  private createSleepingHistogram() {
    const minutes = new Array(60).fill(0);
    for (let i = 0; i < this.events.length - 1; i++) {
      if (this.events[i].type !== EventType.FallAsleep) {
        continue;
      }
      const sleepingFrom = this.events[i].time.getUTCMinutes();
      const sleepingTo = this.events[i + 1].time.getUTCMinutes();
      for (let m = sleepingFrom; m < sleepingTo; m++) {
        minutes[m]++;
      }
      i += 1;
    }
    return minutes;
  }

  private calculateTotalSleepTime() {
    return this.sleepingHistogram.reduce((acc, value) => acc + value, 0);
  }
}

function parseDate(text: string) {
  const timePattern = /\[(\d+-\d+-\d+ \d+:\d+)\]/;
  return new Date(`${text.match(timePattern)![1]} Z`);
}

function parseEventType(text: string) {
  if (text.includes('falls asleep')) {
    return EventType.FallAsleep;
  } else if (text.includes('wakes up')) {
    return EventType.WakeUp;
  } else {
    return EventType.ShiftStart;
  }
}

export function parse(data: string[]) {
  const sortedLines = data.sort((l1, l2) => parseDate(l1).getTime() - parseDate(l2).getTime());

  const guardPattern = /Guard #(\d+) begins shift/;
  const guards: { [id: string]: Guard } = {};
  let guard: Guard | null = null;

  for (let line of sortedLines) {
    const guardId = line.match(guardPattern)?.at(1);
    if (guardId) {
      if (!guards[guardId]) {
        guards[guardId] = new Guard(parseInt(guardId, 10));
      }
      guard = guards[guardId];
    }
    guard?.events.push({ time: parseDate(line), type: parseEventType(line) });
  }

  return guards;
}
