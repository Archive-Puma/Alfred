module.exports = function(grunt) {
    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        watch:
        {
            dev:
            {
                files: [ 'src/**/*' ],
                tasks: ['concat:sass','concat:coffee','pug','sass','coffee','uglify:js'],
            }
        },
        pug:
        {
            compile:
            {
                files: { 'dist/index.html': 'src/pug/index.pug' }
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
                { 'build/alfred.js': 'build/alfred.coffee.md' }
            }
        },
        concat:
        {
            coffee:
            {
                dest: 'build/alfred.coffee.md',
                src: [
                    'src/coffee/methods.coffee.md',
                    'src/coffee/variables.coffee.md',
                    'src/coffee/path.coffee.md',
                    'src/coffee/output.coffee.md',
                    'src/coffee/node.coffee.md',
                    'src/coffee/main.coffee.md'
                ]
            },
            sass:
            {
                dest: 'build/alfred.sass',
                src: [
                    'src/sass/variables.sass',
                    'src/sass/colors.sass',
                    'src/sass/app.sass',
                    'src/sass/node-editor.sass'
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