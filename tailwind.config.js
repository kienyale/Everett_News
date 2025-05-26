/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",  // adjust based on your project
    "./**/*.py"
  ],
  theme: {
    extend: {
      colors: {
        primary: '#2563eb',     // royal blue
        secondary: '#1A5F7A',   // deep teal for hero section
        green: {
          500: '#2563eb',       // override green if needed
          600: '#2563eb',
        },
      },
    },
  },
  plugins: [],
}