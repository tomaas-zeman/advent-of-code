/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.tsx', './styles/index.css'],
  theme: {
    extend: {},
  },
  safelist: [
    {
      pattern: /border-(red|gray|green)-\d00/,
    },
  ],
  plugins: [],
};
