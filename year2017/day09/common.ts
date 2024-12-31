export function processStream(data: string[]) {
  const stack: string[] = [];
  let score = 0;
  let garbage = 0;

  for (const el of data[0].split('')) {
    const top = stack.get(-1);

    if (top === '<') {
      if (el === '>') {
        stack.pop();
      } else if (el === '!') {
        stack.push(el);
      } else {
        garbage++;
      }
      continue;
    } else if (top === '!') {
      stack.pop();
      continue;
    } else if (top === '{') {
      if (el === '}') {
        score += stack.length;
        stack.pop();
        continue;
      }
    }

    if ('{}<!'.includes(el)) {
      stack.push(el);
    }
  }

  return [score, garbage];
}
