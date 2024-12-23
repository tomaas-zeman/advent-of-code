export function loadPolyfills() {
  Array.prototype.asInt = function () {
    return this.map((value) => parseInt(value));
  };
  Array.prototype.get = function (index: number) {
    if (index >= 0) {
      return this[index];
    }
    return this[this.length + index];
  };
}