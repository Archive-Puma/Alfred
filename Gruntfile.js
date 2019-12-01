module.exports = function(grunt) {
    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        watch:
        {
            dev:
            {
                files: [ 'frontend/src/**/*' ],
                tasks: ['concat:sass','concat:coffee','pug','sass','coffee','uglify:js'],
            }
        },
        pug:
        {
            compile:
            {
                files: { 'dist/index.html': 'frontend/src/pug/index.pug' }
            }
        },
        sass:
        {
            compile:
            {
                options:
                {
                    sourcemap: 'none',
                    style: 'compressed',
                    noCache: true
                },
                files: { 'dist/css/alfred.min.css': 'build/alfred.sass' }
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
                {
                    'main.js': 'frontend/src/coffee/electron.coffee.md', // Dev
                    'dist/main.js': 'frontend/src/coffee/electron.coffee.md',
                    'build/alfred.js': 'build/alfred.coffee.md'
                }
            }
        },
        concat:
        {
            coffee:
            {
                dest: 'build/alfred.coffee.md',
                src: [
                    'frontend/src/coffee/variables.coffee.md',
                    'frontend/src/coffee/methods.coffee.md',
                    'frontend/src/coffee/path.coffee.md',
                    'frontend/src/coffee/output.coffee.md',
                    'frontend/src/coffee/node.coffee.md',
                    'frontend/src/coffee/work2node.coffee.md',
                    'frontend/src/coffee/python2js.coffee.md',
                    'frontend/src/coffee/main.coffee.md'
                ]
            },
            sass:
            {
                dest: 'build/alfred.sass',
                src: [
                    'frontend/src/sass/variables.sass',
                    'frontend/src/sass/colors.sass',
                    'frontend/src/sass/app.sass',
                    'frontend/src/sass/windowbar.sass',
                    'frontend/src/sass/modal.sass',
                    'frontend/src/sass/node-editor.sass'
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

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-pug');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-coffee');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.registerTask('dev', ['watch:dev']);
    grunt.registerTask('compile', ['concat:sass','concat:coffee','pug','sass','coffee','uglify:js']);
};