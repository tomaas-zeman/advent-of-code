import "mathjs";

//-----------------
//     ARRAYS     -
//-----------------

declare global {
  interface Array<T> {
    /**
     * Returns an item from an array.
     * Index can be negative whereas -1 is the last element.
     * 
     * @param index array index
     */
    get(index: number): T;
  }
}

//-------------------
//     MATRICES     -
//-------------------

declare module 'mathjs' {
  interface Matrix {
    getRow(rowIndex: number): Matrix;
    getColumn(colIndex: number): Matrix;
  }
}

export {}