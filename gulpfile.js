var gulp = require("gulp");
var crass = require('gulp-crass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var htmlmin = require('gulp-htmlmin');


// Script paths
var build = 'build';
var styles = 'src/css/**/*.css';
var scripts = [
    'src/js/engine/litegraph.js',
    'src/js/engine/initialize.js',
    'src/js/nodes/**/*.js',
    'src/js/engine/default.js'
];

var js = function() {
    return gulp.src(scripts)
        .pipe(concat('alfred.js'))
        .pipe(uglify())
        .pipe(gulp.dest(build));
}, css = function() {
    return gulp.src(styles)
        .pipe(concat('alfred.css'))
        .pipe(crass({pretty:false}))
        .pipe(gulp.dest(build));
}, html = function() {
    return gulp.src('src/index.html')
        .pipe(htmlmin({ collapseWhitespace: true }))
        .pipe(gulp.dest(build));
}, dev = function() {
    return gulp.watch(scripts, gulp.series(js));
}

gulp.task('js', js);
gulp.task('css', css);
gulp.task('dev', dev);
gulp.task('html', html);