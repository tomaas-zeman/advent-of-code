import { Point3D } from "../../aocutils";

type Particle = {
  id: number;
  position: Point3D;
  velocity: Point3D;
  acceleration: Point3D;
};

export function parse(data: string[]) {
  const particles: Particle[] = [];

  for (const line of data) {
    const [px, py, pz, vx, vy, vz, ax, ay, az] = line.match(/(-?\d+)/g)!.asInt();
    particles.push({
      id: particles.length,
      position: [px, py, pz],
      velocity: [vx, vy, vz],
      acceleration: [ax, ay, az],
    });
  }

  return particles;
}