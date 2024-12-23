export type BisectRangeDirection = 'left' | 'right';

export class BisectRange {
  private left: number;
  private right: number;
  private direction: BisectRangeDirection;

  current: number;

  constructor(left: number, right: number) {
    this.left = left;
    this.right = right;
    this.current = right;
    this.direction = 'left';
  }

  setDirection(direction: BisectRangeDirection) {
    this.direction = direction;
  }

  next() {
    switch (this.direction) {
      case 'left':
        this.right = this.current;
        break;
      case 'right':
        this.left = this.current;
        break;
    }
    this.current = Math.floor((this.left + this.right) / 2);
    return this.current;
  }

  hasNext() {
    return this.left < this.right - 1;
  }
}
