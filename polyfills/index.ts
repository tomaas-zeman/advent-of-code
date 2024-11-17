import { Matrix, flatten, subset, index, range } from 'mathjs';

//-------------------
//     MATRICES     -
//-------------------

(function enableMathJSPolyfills() {
  Matrix.prototype.getRow = function (rowIndex: number): Matrix {
    return flatten(subset(this, index(rowIndex, range(0, this.size()[1]))));
  };

  Matrix.prototype.getColumn = function (colIndex: number): Matrix {
    return flatten(subset(this, index(range(0, this.size()[0]), colIndex)));
  };
})();