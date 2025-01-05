import { HashSet, isEqual } from '../../aocutils';

type Component = [number, number];

export function constructBridges(data: string[]) {
  const components = data.map((line) => line.split('/').asInt()) as Component[];
  const grounds = components.filter(([a, b]) => a === 0 || b === 0);

  const bridges: Component[][] = [];

  function createBridge(
    usedComponents: Component[],
    availableComponents: HashSet<Component>,
    lastPort: number,
  ) {
    bridges.push(usedComponents);

    for (const component of availableComponents.values()) {
      const nextPort =
        component[0] === lastPort ? component[1] : component[1] === lastPort ? component[0] : null;
      if (nextPort != null) {
        const nextUsedComponents = [...usedComponents, component];
        const nextAvailableComponents = availableComponents.clone();
        nextAvailableComponents.delete(component);
        createBridge(nextUsedComponents, nextAvailableComponents, nextPort);
      }
    }
  }

  for (const ground of grounds) {
    const availableComponents = new HashSet(components.filter((c) => !isEqual(c, ground)));
    createBridge([ground], availableComponents, ground[0] === 0 ? ground[1] : ground[0]);
  }

  return bridges;
}
