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
