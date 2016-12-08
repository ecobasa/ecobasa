![ecobasa logo](http://cloud.ecobasa.org/public.php?service=files&t=976069b03a5d7f4153c5cfc16e7ab309&download)

Repository of http://ecobasa.org

# Requisites
* Django (Python)
* PostgreSQL
* LESS (use node.js Grunt or Compass to compile CSS)

Environment Requirements
------------

	$ pip install -r requirements.txt


Database
--------

We use PostgreSQL: http://www.postgresql.org/
For OSX we recommend: http://postgresapp.com/
See http://od-eon.com/blogs/calvin/postgresql-cheat-sheet-beginners/
for a bit of setup info. Basically:

	$ sudo su - postgres
	$ createuser django -P # enter password, answer no to all questions
	$ createdb -E utf8 -O django ecobasa -T template0

As user posgres, you might have to check /etc/postgresql/9.1/main/pg_hba.conf
if the TYPE 'local' for USER 'all' has METHOD set to 'md5' .

Afterwards you should be able to bootstrap the database as your normal user:

	$ ./manage.py syncdb --noinput
	$ ./manage.py migrate
	$ ./manage.py createsuperuser

Note: Running `syncdb` with `--noinput` is important, as otherwise setting up
the superuser will fail due to tables which would only be created at migration
time.


Running
-------

Before running in production mode, you should collect the static files:

	$ ./manage.py collectstatic

which will collect all apps' static files into the directory static/ .


Run it:

	$ ./manage.py runserver


Set up your Django site
-----------------------

For some features, e.g. user registration to work properly, it is necessary to
set up a Django site, go to http://localhost:8000/admin/sites/site/1/ and edit
the appropriate domain and display name (use the super user account created
earlier to log in).


If you don't have a site defined in your database and django wants to reference it, you will need to create one.

From a python manage.py shell :

	$ from django.contrib.sites.models import Site
	$ new_site = Site.objects.create(domain='foo.com', name='foo.com')
	$ print new_site.id

Now set that site ID in your settings.py to SITE_ID



Set up the special group
------------------------

Edit your local settings.py for ECOBASA_SPECIAL_COSINNUS_GROUP to point to the
primary key of the special group every pioneer will become a member of and
whose blog posts are exposed. You will have to do that after setting up the
group in the admin interface.
