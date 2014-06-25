var gulp = require('gulp'),
  stylus = require('gulp-stylus'),
  connect = require('gulp-connect');

gulp.task('connect', function() {
  connect.server({
    root: 'www',
    livereload: true
  });
});

gulp.task('html', function () {
  gulp.src('./www/*.html')
    .pipe(connect.reload());
});

gulp.task('stylus', function () {
  gulp.src('./www/stylus/*.styl')
    .pipe(stylus())
    .pipe(gulp.dest('./www/css/compiled'))
    .pipe(connect.reload());
});

gulp.task('watch', function () {
  gulp.watch(['./www/*.html'], ['html']);
  gulp.watch(['./www/stylus/*.styl'], ['stylus']);
});

gulp.task('default', ['stylus', 'connect', 'watch']);