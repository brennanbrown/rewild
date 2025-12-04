/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,njk,md}"],
  theme: {
    extend: {
      colors: {
        forest: "#22543d",
        moss: "#4a7c59",
        earth: "#7b4f2c",
        sky: "#2b6cb0",
        sand: "#f5f0e6"
      },
      fontFamily: {
        display: ["system-ui", "-apple-system", "BlinkMacSystemFont", "Segoe UI", "sans-serif"],
        body: ["system-ui", "-apple-system", "BlinkMacSystemFont", "Segoe UI", "sans-serif"]
      }
    }
  },
  plugins: [
    require("@tailwindcss/typography")
  ]
};
