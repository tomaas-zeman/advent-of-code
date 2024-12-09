import { createRef, RefObject, useEffect, useRef } from 'react';
import { VisualizerProps } from '..';
import range from 'lodash/range';

type Config = {
  areaSize: [number, number];
  antennas: { [frequency: string]: [number, number][] };
};

type Antinode = { antinode: [number, number] };

function createGridRefs([rows, cols]: [number, number]) {
  const gridRefs: RefObject<HTMLDivElement>[][] = [];
  for (let row = 0; row < rows; row++) {
    const row = [];
    for (let col = 0; col < cols; col++) {
      row.push(createRef<HTMLDivElement>());
    }
    gridRefs.push(row);
  }
  return gridRefs;
}

function renderGrid([rows, cols]: [number, number], gridRefs: RefObject<HTMLDivElement>[][]) {
  const classNames = 'w-1/2 h-1/2 self-center absolute opacity-0 antinode transition-opacity';
  const style = { filter: 'invert(1)' };

  return (
    <div
      className={`grid grid-cols-12 gap-4`}
      style={{ maxWidth: `${cols * 2.5 + (cols - 1)}rem` }}
    >
      {range(0, rows).map((row) =>
        range(0, cols).map((col) => (
          <div
            ref={gridRefs[row][col]}
            className="
              flex
              w-10 h-10 
              rounded-full border-2 border-gray-500
              place-content-center relative"
          >
            <img
              src="src/visualizers/2024-08/assets/antinode.png"
              className={`${classNames} antinode`}
              style={style}
            />
            <img
              src="src/visualizers/2024-08/assets/radio-tower.png"
              className={`${classNames} tower`}
              style={style}
            />
          </div>
        )),
      )}
    </div>
  );
}

function setTileImageOpacity(
  tileRef: RefObject<HTMLDivElement>,
  opacity: number,
  tile: 'tower' | 'antinode',
) {
  const image = tileRef.current?.getElementsByClassName(tile)[0] as HTMLDivElement;
  image.style.opacity = opacity.toString();
}

export default function Visualizer(props: VisualizerProps) {
  const { antennas, areaSize } = useRef(props.buffer[0] as Config).current;
  const antinodes = useRef(
    (props.buffer.slice(1) as Antinode[]).map((item) => item.antinode),
  ).current;
  const gridRefs = useRef(createGridRefs(areaSize));

  useEffect(() => {
    for (const antenna of Object.values(antennas)) {
      for (const [row, col] of antenna) {
        const tileRef = gridRefs.current[row][col];
        tileRef.current?.classList.add('border-green-300');
        setTileImageOpacity(tileRef, 1, 'tower')
      }
    }
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      const antinode = antinodes.shift();
      if (!antinode || !props.runVisualization) {
        clearInterval(interval);
        props.onVisualizationEnd();
        return;
      }

      const isAlsoAntennaTile = Object.values(antennas).find((antenna) =>
        antenna.find(([row, col]) => antinode[0] === row && antinode[1] === col),
      );

      const tileRef = gridRefs.current[antinode[0]][antinode[1]];
      setTileImageOpacity(tileRef, 1, 'antinode');

      if (isAlsoAntennaTile) {
        setTileImageOpacity(tileRef, 0, 'tower');
        tileRef.current?.classList.add('border-orange-300');
      } else {
        tileRef.current?.classList.add('border-red-300');
      }
    }, 500);

    return () => clearInterval(interval);
  }, [props.runVisualization]);

  return renderGrid(areaSize, gridRefs.current);
}
