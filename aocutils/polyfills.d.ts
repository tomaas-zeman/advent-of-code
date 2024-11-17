import * as m from 'mathjs';

//-------------------
//     MATRICES     -
//-------------------

declare module 'mathjs' {
  interface Matrix {
    getRow(rowIndex: number): m.Matrix;
    getColumn(colIndex: number): m.Matrix;
  }
}
