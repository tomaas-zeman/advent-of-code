import { VisualizerProps } from '../visualizers';
import { useEffect, useRef } from 'react';
import cytoscape from 'cytoscape';

export default function TestVisualizer(props: VisualizerProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    cytoscape({
      container: containerRef.current,
      elements: [
        { data: { id: 'A' }, style: { 'background-color': 'green' } },
        { data: { id: 'B' } },
        { data: { id: 'C' } },
        { data: { id: 'D' } },
        { data: { id: 'E' }, style: { 'background-color': 'red' } },
        { data: { source: 'A', target: 'B' } },
        { data: { source: 'A', target: 'C' } },
        { data: { source: 'C', target: 'E' } },
        { data: { source: 'B', target: 'D' } },
        { data: { source: 'B', target: 'E' } },
        { data: { source: 'D', target: 'E' } },
      ],
      layout: {
        name: 'concentric',
        avoidOverlap: true,
        minNodeSpacing: 100,
      },
      style: [
        {
          selector: 'node',
          style: {
            label: 'data(id)',
            color: 'white',
            'text-valign': 'center',
            'text-halign': 'center',
          },
        },
        {
          selector: 'edge',
          style: {
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'arrow-scale': 1.5,
          },
        },
      ],
    });
  }, []);

  return (
    <>
      <div ref={containerRef} className="h-[50vh]" />
    </>
  );
}
