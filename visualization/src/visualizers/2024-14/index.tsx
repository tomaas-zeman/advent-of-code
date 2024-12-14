import { useEffect, useRef } from 'react';
import { VisualizerProps } from '..';

const scale = 8;
const fps = 1000;

type Robot = { x: number; y: number; vx: number; vy: number };
type Robots = { robots: Robot[] }[];
type Config = { width: number; height: number; step: number };

function renderRobot(context: CanvasRenderingContext2D, robot: Robot, frame: number) {
  context.fillStyle = 'rgb(66, 165, 245)';
  context.fillRect(
    (robot.x + (robot.vx / fps) * frame) * scale,
    (robot.y + (robot.vy / fps) * frame) * scale,
    5,
    5,
  );
}

function glow(context: CanvasRenderingContext2D, robots: Robot[]) {
  // Empirical (only for simple animation): 28, 61, 28, 59
  const tree = robots.filter(
    (robot) => robot.x >= 28 && robot.x <= 61 && robot.y >= 28 && robot.y <= 61,
  );
  context.shadowColor = 'yellow';
  context.shadowBlur = 20;

  for (const robot of tree) {
    renderRobot(context, robot, 0);
  }
}

export default function Visualizer(props: VisualizerProps) {
  const robots = useRef(props.buffer.slice(0, -1) as Robots).current;
  const { width, height, step } = useRef(props.buffer.slice(-1)[0] as Config).current;
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frame = useRef(-1000);

  useEffect(() => {
    if (!props.runVisualization) {
      return;
    }

    const canvas = canvasRef.current!;
    const ctx = canvas.getContext('2d')!;

    const draw = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (const robot of robots[step].robots) {
        renderRobot(ctx, robot, frame.current);
      }
      frame.current++;
    };

    const animate = () => {
      if (frame.current - 1 === 0) {
        glow(ctx, robots[step].robots);
        return;
      }
      draw();
      requestAnimationFrame(animate);
    };
    animate();
  }, [props.runVisualization]);

  return (
    <>
      <canvas ref={canvasRef} width={width * scale} height={height * scale} className="border-2" />
    </>
  );
}
