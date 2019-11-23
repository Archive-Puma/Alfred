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
                files: { 'frontend/dist/index.html': 'frontend/src/pug/index.pug' }
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
                files: { 'frontend/dist/css/alfred.min.css': 'frontend/build/alfred.sass' }
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
                { 'frontend/build/alfred.js': 'frontend/build/alfred.coffee.md' }
            }
        },
        concat:
        {
            coffee:
            {
                dest: 'frontend/build/alfred.coffee.md',
                src: [
                    'frontend/src/coffee/variables.coffee.md',
                    'frontend/src/coffee/methods.coffee.md',
                    'frontend/src/coffee/path.coffee.md',
                    'frontend/src/coffee/output.coffee.md',
                    'frontend/src/coffee/node.coffee.md',
                    'frontend/src/coffee/work2node.coffee.md',
                    'frontend/src/coffee/main.coffee.md'
                ]
            },
            sass:
            {
                dest: 'frontend/build/alfred.sass',
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
                files: { 'frontend/dist/js/alfred.min.js': 'frontend/build/alfred.js' }
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