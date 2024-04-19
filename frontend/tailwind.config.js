/** @type {import('tailwindcss').Config} */
module.exports = {

  theme: {
    extend: {},
  },
  plugins: [],
  content: [
    '../templates/**/*.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
    './src/views/*.vue'
  ],
}

