export function collapsePolymer(initialPolymer: string) {
  const polymer = initialPolymer.split('');

  for (let i = 0; i < polymer.length - 1; i++) {
    const l = polymer[i];
    const r = polymer[i + 1];
    if (l !== r && l.toLowerCase() === r.toLowerCase()) {
      polymer.splice(i, 2);
      i = Math.max(-1, i - 2);
    }
  }

  return polymer.length;
}
