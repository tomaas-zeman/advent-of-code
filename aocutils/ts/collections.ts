import { TypeGuard } from './utils';

export type PriorityQueueItem<T> = { priority: number } & T;

export class PriorityQueue<T> {
  private queue: PriorityQueueItem<T>[] = [];

  constructor(initialItems: PriorityQueueItem<T>[] = []) {
    initialItems.forEach((item) => this.enqueue(item));
  }

  enqueue(item: PriorityQueueItem<T>) {
    if (this.size() === 0) {
      this.queue.push(item);
      return;
    }

    for (let i = 0; i < this.queue.length; i++) {
      if (item.priority < this.queue[i].priority) {
        this.queue.splice(i, 0, item);
        return;
      }
    }

    this.queue.push(item);
  }

  dequeue() {
    return this.queue.shift();
  }

  peek(): PriorityQueueItem<T> | undefined {
    return this.queue[0];
  }

  size() {
    return this.queue.length;
  }
}

//---------------
//     MAPS     -
//---------------

type DefaultValue<T> = T | (() => T);

export class DefaultMap<K, V> extends Map<K, V> {
  private defaultValue: DefaultValue<V>;
  private hashKeys: boolean;

  constructor(defaultValue: DefaultValue<V>, iterable?: Iterable<[K, V]>, hashKeys = false) {
    super(iterable);
    this.defaultValue = defaultValue;
    this.hashKeys = hashKeys;
  }

  private getDefaultValue() {
    return TypeGuard.isFunction(this.defaultValue) ? this.defaultValue() : this.defaultValue;
  }

  get(key: K): V {
    key = this.getKey(key);
    let value = super.get(key);
    if (value === undefined) {
      value = this.getDefaultValue();
      super.set(key, value);
    }
    return value;
  }

  set(key: K, value: V) {
    return super.set(this.getKey(key), value);
  }

  has(key: K) {
    return super.has(this.getKey(key));
  }

  delete(key: K) {
    return super.delete(this.getKey(key));
  }

  keys() {
    if (!this.hashKeys) {
      return super.keys();
    }
    return super.keys().map((k) => JSON.parse(k as string) as K);
  }

  mapItem(key: K, mappingFn: (value: V) => V) {
    this.set(key, mappingFn(this.get(key)));
  }

  private getKey(key: K) {
    return this.hashKeys ? (JSON.stringify(key) as K) : key;
  }
}

//---------------
//     SETS     -
//---------------

export class HashSet<T> extends Set {
  constructor(initialItems: Iterable<T> = []) {
    super();
    for (const item of initialItems) {
      this.add(item);
    }
  }

  add(value: T) {
    return super.add(JSON.stringify(value));
  }

  has(value: T) {
    return super.has(JSON.stringify(value));
  }

  delete(value: T) {
    return super.delete(JSON.stringify(value));
  }

  *values(): SetIterator<T> {
    for (const item of super.values()) {
      yield JSON.parse(item);
    }
  }

  clone(): HashSet<T> {
    return new HashSet(this.values());
  }
}
