/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: [
          '-apple-system',
          'BlinkMacSystemFont',
          '"SF Pro Display"',
          '"SF Pro Text"',
          'Inter',
          'system-ui',
          'sans-serif',
        ],
        mono: ['"SF Mono"', '"Fira Code"', 'Menlo', 'Monaco', 'monospace'],
      },
      colors: {
        apple: {
          blue: '#0071E3',
          'blue-hover': '#0077ED',
          'blue-active': '#006EDB',
          gray: {
            50: '#F5F5F7',
            100: '#E8E8ED',
            200: '#D2D2D7',
            300: '#AEAEB2',
            400: '#8E8E93',
            500: '#636366',
            600: '#48484A',
            700: '#3A3A3C',
            800: '#2C2C2E',
            900: '#1C1C1E',
          },
        },
        status: {
          pending: '#FF9F0A',
          in_progress: '#0071E3',
          done: '#30D158',
        },
      },
      borderRadius: {
        apple: '12px',
        'apple-sm': '8px',
        'apple-lg': '18px',
        'apple-xl': '24px',
      },
      backdropBlur: {
        apple: '20px',
      },
      boxShadow: {
        apple: '0 2px 20px rgba(0,0,0,0.08)',
        'apple-md': '0 4px 30px rgba(0,0,0,0.12)',
        'apple-lg': '0 8px 40px rgba(0,0,0,0.16)',
        'apple-inset': 'inset 0 1px 0 rgba(255,255,255,0.1)',
      },
      animation: {
        'fade-in': 'fadeIn 0.2s ease-out',
        'slide-up': 'slideUp 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)',
        'scale-in': 'scaleIn 0.2s cubic-bezier(0.34, 1.56, 0.64, 1)',
      },
      keyframes: {
        fadeIn: { from: { opacity: 0 }, to: { opacity: 1 } },
        slideUp: { from: { opacity: 0, transform: 'translateY(8px)' }, to: { opacity: 1, transform: 'translateY(0)' } },
        scaleIn: { from: { opacity: 0, transform: 'scale(0.95)' }, to: { opacity: 1, transform: 'scale(1)' } },
      },
    },
  },
  plugins: [],
}
