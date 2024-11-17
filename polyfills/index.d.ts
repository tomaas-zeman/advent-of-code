import 'mathjs';

//-------------------
//     MATRICES     -
//-------------------

declare module 'mathjs' {
  interface Matrix {
    getRow(rowIndex: number): Matrix;
    getColumn(colIndex: number): Matrix;
  }
}
