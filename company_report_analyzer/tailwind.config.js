module.exports = {
  content: [
    './templates/**/*.html',  // Путь к HTML-шаблонам в папке templates
    './static/js/**/*.js',    // Путь к JS-файлам, если используются динамические классы
    './report_analyzer/**/*.html',  // Если есть HTML-шаблоны в приложениях
  ],
  theme: {
    extend: {
      colors: {
        'custom': 'rgb(61, 61, 61)', 
        'cstm-blue': 'rgb(13, 176, 198)', 
      },
    },
  },
  plugins: [],
}

