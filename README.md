ALPHA
=====

Name: cmsplugin-plaintext
Description: Adds a plaintext plugin for django-cms.
Download: http://bitbucket.org/xenofox/cmsplugin-plaintext/

Forked/cloned to add django-cms 3 and south migrations support
--------------------------------------------------------------

Requirements:

* django-cms-3.0

Last tested with:

* django-cms-3.0.3
* django: 1.6.5

Setup

* make sure requirements are installed and properly working
* add cmsplugin_plaintext to python path
* add 'cmsplugin_plaintext' to INSTALLED_APPS
* run 'python manage.py syncdb'

Migrate from version 0.1 (and djangocms 2)

* run 'python manage.py migrate cmsplugin_plaintext 0001 --fake' (existing table)
* run 'python manage.py migrate cmsplugin_plaintext' (to rename the table to cms 3 format)

TODO:

* Add tests
* Add translations
