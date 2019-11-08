module.exports = function(grunt) {
    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        pug:
        {
            compile:
            {
                files: { 'dist/index.html': 'src/index.pug' }
            }
        },
        sass:
        {
            compile:
            {
                options:
                {
                    noSourceMap: true,
                    style: 'compressed'
                },
                files: { 'dist/css/alfred.min.css': 'src/sass/node-editor.sass' }
            }
        },
        coffee:
        {
            compile:
            {
                options:
                {
                    bare: true
                },
                files:
                { 'build/alfred.js': 'build/alfred.coffee.md' }
            }
        },
        concat:
        {
            coffee:
            {
                dest: 'build/alfred.coffee.md',
                src: [
                    'src/coffee/variables.coffee.md',
                    'src/coffee/functions.coffee.md',
                    'src/coffee/node.coffee.md',
                    'src/coffee/main.coffee.md'
                ]
            }
        },
        uglify:
        {
            js:
            {
                files: { 'dist/js/alfred.min.js': 'build/alfred.js' }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-pug');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-coffee');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.registerTask('compile', ['pug','sass', 'concat:coffee', 'coffee', 'uglify:js']);
};