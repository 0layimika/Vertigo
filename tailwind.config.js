/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    colors: {
      "dark-red": "hsla(0,70%,35%,0.8)",
      cream: "hsla(40,60%,95%,1)",
      "cream-dark": "hsla(40,60%,85%,1)",
      grey: "#F3F3F3",
      "grey-btn" : "#808080",
      "soft-black": "hsla(0,0%,10%,0.8)",
      beige: "hsla(40,50%,70%,0.8)",
      gold: "hsla(40,60%,65%,0.8)",
      "soft-blue": "hsla(200,60%,65%,0.8)",
      white: "hsla(0,100%,100%,1)",
      black: "hsla(0,0%,0%,1)",
    },
    screens: {
      xs: "450px",
      xsm: "500px",
      s: '600px',
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
      "2xl": "1536px",
    },

    fontFamily: {
      main: ["Montserrat", "sans-serif"],
      serif : ['Playfair Display', 'serif']
    },
    extend: {
      boxShadow: {
        custom: "4px -3px 10px 0px rgba(0, 0, 0, 0.25)",
      },
    },
  },
  plugins: [],
};
