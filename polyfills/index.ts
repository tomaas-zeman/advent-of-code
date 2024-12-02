import { Matrix, flatten, subset, index, range } from 'mathjs';

//-----------------
//     ARRAYS     -
//-----------------

Array.prototype.get = function <T>(index: number): T {
  if (index >= 0) {
    return this[index];
  }
  return this[this.length + index];
};

//-------------------
//     MATRICES     -
//-------------------

Matrix.prototype.getRow = function (rowIndex: number): Matrix {
  return flatten(subset(this, index(rowIndex, range(0, this.size()[1]))));
};

Matrix.prototype.getColumn = function (colIndex: number): Matrix {
  return flatten(subset(this, index(range(0, this.size()[0]), colIndex)));
};
