/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
	  './musicapp/**/*.{html, js}',
	  'node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
	  require('@tailwindcss/forms'),
	  require('preline/plugin'),
  ],
}
