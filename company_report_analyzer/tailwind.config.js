module.exports = {
  content: [
    './templates/**/*.html',  // Путь к HTML-шаблонам в папке templates
    './static/js/**/*.js',    // Путь к JS-файлам, если используются динамические классы
    './report_analyzer/**/*.html',  // Если есть HTML-шаблоны в приложениях
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

