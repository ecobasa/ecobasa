<<<<<<< HEAD
ecobasa_uanoa
=============

Relaunch of http://ecobasa.org


Database
--------

We use PostgreSQL: http://www.postgresql.org/.
See http://od-eon.com/blogs/calvin/postgresql-cheat-sheet-beginners/
for a bit of setup info. Basically:

	$ sudo su - postgres
	$ createuser django -P # enter password, answer no to all questions
	$ createdb -E utf8 -O django ecobasa_uanoa -T template0

As user posgres, you might have to check /etc/postgresql/9.1/main/pg_hba.conf
if the TYPE 'local' for USER 'all' has METHOD set to 'md5' . Afterwards you
should be able to syncdb as your normal user:

	$ ./manage.py syncdb


Running
-------

Before running in production mode, you should collect the static files:

	$ ./manage.py collectstatic

which will collect all apps' static files into the directory static/ .


Run it:

	$ ./manage.py runserver
=======
ecobasa-UaNoa
=============

ecobasa 2.0
>>>>>>> c60d6f2057e0e24b6ce739f4bbc49d12f0bd28bf
