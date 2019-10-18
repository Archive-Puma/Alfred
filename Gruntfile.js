module.exports = function(grunt)
{
    // Project configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        watch: {
            options: {
                spawn: false,
                interrupt: true
            },
            sass: {
                tasks: ['pug','sass'],
                files: ['src/index.pug','src/scss/*.scss']
            }
        },

        pug: {
            dist: {
                files: { 'dist/index.html' : 'src/index.pug' }
            }
        },
        sass: {
            dist: {
                files: [{
                    expand: true,
                    cwd: 'src/scss',
                    src: ['*.scss'],
                    dest: 'dist/css',
                    ext: '.css'
                }],
                options: {
                    style: 'compressed'
                }
            }
        },
        copy: {
            js: {
                expand: true,
                cwd: 'src',
                src: 'js/**/*',
                dest: 'dist/'
            },
            assets: {
                expand: true,
                cwd: 'src',
                src: 'assets/**/*',
                dest: 'dist/'
            }
        }
    });
    // Contrib-Modules
    grunt.loadNpmTasks('grunt-contrib-pug');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-watch');
    
    // Tasks
    grunt.registerTask('dist', ['pug','sass','copy:js','copy:assets']);
}