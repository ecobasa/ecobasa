'use strict';

module.exports = function (grunt) {

    // load all grunt tasks
    require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

    var base = 'ecobasa/static';

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        watch: {
            sass: {
                files: '**/*.s[ac]ss',
                tasks: ['sass:dev']
            },
            options: {
                livereload: 35731,
            },
        },
        sass: {                              // Task
            dev: {                             // Another target
                options: {                       // Target options
                    style: 'expanded',
                    trace: true
                    /* lineNumbers: true */
                },
                files: {
                    'ecobasa/static/css/main.css': base + '/sass/main.scss'
                    //'forum/static/forum/css/main.css': 'forum/' + base + '/forum/sass/main.scss',
                }
            }
        }
    });
    grunt.registerTask('default', [
        'sass', 'watch'
    ]);
};