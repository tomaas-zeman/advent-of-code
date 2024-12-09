import {
  createRef,
  Dispatch,
  forwardRef,
  RefObject,
  SetStateAction,
  useEffect,
  useRef,
  useState,
} from 'react';
import { VisualizerProps } from '..';

type Data = {
  numbers: number[];
  counts: { [key: number]: number };
};

type CircleProps = { number: number; count: number };
type CircleRefs = { [key: string]: RefObject<HTMLDivElement> };

function randomPosition(min: number, max: number) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

function getCoords(el: HTMLElement) {
  const { left, top, width, height } = el.getBoundingClientRect();
  const x = Math.floor(left + width / 2);
  const y = Math.floor(top + height / 2);
  return [x, y];
}

function processCircle(
  circleId: number,
  number: number,
  count: number,
  resultDiv: HTMLDivElement,
  circleRefs: CircleRefs,
  total: number,
  setTotal: Dispatch<SetStateAction<number>>,
) {
  const circle = circleRefs[circleId].current;
  if (!circle) {
    return;
  }

  const [sourceX, sourceY] = getCoords(circle);
  const [targetX, targetY] = getCoords(resultDiv);
  const translateX = targetX - sourceX;
  const translateY = targetY - sourceY;

  circle.style.backgroundColor = '#ff9494';
  circle.style.zIndex = '99';
  setTimeout(() => {
    circle.style.transform = `translate(${translateX}px, ${translateY}px)`;
    circle.addEventListener(
      'transitionend',
      () => {
        circle.style.opacity = '0';
        setTotal(total + number * count);
      },
      { once: true },
    );
  }, 300);
}

const Circle = forwardRef<HTMLDivElement, CircleProps>(({ number, count }, ref) => {
  const [position, _] = useState({
    x: randomPosition(10, 70),
    y: randomPosition(40, 90),
  });

  return (
    <div
      ref={ref}
      id={number.toString()}
      className="
        fixed
        w-20 h-20 rounded-full
        bg-gray-500
        shadow-[0_0_40px_-10px] shadow-gray-200
        text-center content-center"
      style={{
        left: `${position.x}vw`,
        top: `${position.y}vh`,
        transition: 'transform 2s ease, opacity 0.5s ease',
      }}
    >
      <span className="font-bold text-lg">{number}</span>
      <span className="text-xs block">{count || 0}x</span>
    </div>
  );
});

export default function Visualizer(props: VisualizerProps) {
  const { numbers, counts } = useRef(props.buffer[0] as Data).current;
  const numbersIndex = useRef(0);

  const resultDivRef = useRef<HTMLDivElement>(null);
  const circleRefs = useRef({} as CircleRefs);

  const [total, setTotal] = useState(0);

  useEffect(() => {
    Object.keys(numbers).forEach((i) => {
      circleRefs.current[i] = createRef<HTMLDivElement>();
    });
  }, [counts]);

  useEffect(() => {
    const resultDiv = resultDivRef.current;
    if (props.runVisualization && resultDiv) {
      while (true) {
        if (numbersIndex.current >= numbers.length) {
          return;
        }
        if (counts[numbers[numbersIndex.current]]) {
          break;
        }
        numbersIndex.current++;
      }
      
      processCircle(
        numbersIndex.current,
        numbers[numbersIndex.current],
        counts[numbers[numbersIndex.current]],
        resultDiv,
        circleRefs.current,
        total,
        setTotal,
      );
      numbersIndex.current++;
    }
  }, [total, props.runVisualization]);

  return (
    <>
      <div className="w-full h-[50vh]">
        <div
          ref={resultDivRef}
          className={`
            fixed top-56 right-36
            w-36 h-36 rounded-full
            bg-green-600
            shadow-[0_0_50px_10px] shadow-green-700
            text-center content-center`}
        >
          <span className="font-bold text-lg block">TOTAL</span>
          <span>{total}</span>
        </div>
        {numbers.map((number, i) => (
          <Circle key={i} ref={circleRefs.current[i]} number={number} count={counts[number] ?? 0} />
        ))}
      </div>
    </>
  );
}
