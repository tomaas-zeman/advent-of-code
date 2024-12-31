export function processStream(data: string[]): [number, number] {
  const stack: string[] = [];
  let score = 0;
  let garbage = 0;

  for (const el of data[0].split('')) {
    const top = stack[stack.length - 1];

    if (top === '<') {
      if (el === '>') {
        stack.pop();
      } else if (el === '!') {
        stack.push(el);
      } else {
        garbage++;
      }
    } else if (top === '!') {
      stack.pop();
    } else if (top === '{' && el === '}') {
      score += stack.length;
      stack.pop();
    } else if ('{}<!'.includes(el)) {
      stack.push(el);
    }
  }

  return [score, garbage];
}
