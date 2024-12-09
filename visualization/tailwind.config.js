/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.tsx', './styles/index.css'],
  theme: {
    extend: {
      gridTemplateColumns: {
        450: 'repeat(450, minmax(0, 1fr))',
      },
    },
  },
  safelist: [
    {
      pattern: /border-(red|gray|green)-\d00/,
    },
    {
      pattern: /bg-(red|gray|green)-\d00/,
    },
  ],
  plugins: [],
};
