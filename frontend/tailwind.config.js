/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#65C3C8",
        secondary: "#EF9FBC",
        teritiary: "#EEAF3A",
        quaternary: "#291334",
        white: "#FAF7F5",
      },
    },
  },
  darkMode: "class",
  daisyui: {
    themes: ["cupcake"],
  },
  // eslint-disable-next-line no-undef
  plugins: [require("daisyui")],
};
