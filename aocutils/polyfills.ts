import * as m from 'mathjs';

//-------------------
//     MATRICES     -
//-------------------

export function enableMathJSPolyfills() {
  m.Matrix.prototype.getRow = function (rowIndex: number): m.Matrix {
    return m.flatten(m.subset(this, m.index(rowIndex, m.range(0, this.size()[1]))));
  };

  m.Matrix.prototype.getColumn = function (colIndex: number): m.Matrix {
    return m.flatten(m.subset(this, m.index(m.range(0, this.size()[0]), colIndex)));
  };
}
