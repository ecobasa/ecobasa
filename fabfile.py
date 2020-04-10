from fabric.api import *  # noqa

def production():
    env.hosts = ['root@strix.ecobytes.net -p666']
    env.path = '/data/domains/ecobasa.org/src/'
    env.push_branch = 'master'
    env.push_remote = 'origin'

def update():
    with cd(env.path):
        run("git pull %(push_remote)s %(push_branch)s" % env)
        run("docker-compose build django")
        run("docker-compose run --rm django ./manage.py collectstatic --noinput")

def migrate():
    with cd(env.path):
        run("docker-compose run --rm django ./manage.py syncdb")
        run("docker-compose run --rm django ./manage.py migrate")

def reload():
    with cd(env.path):
        run("docker-compose stop django && docker-compose rm -f django && docker-compose up -d django")

def deploy():
    update()
    migrate()
    reload()
