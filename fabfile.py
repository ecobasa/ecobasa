from fabric.api import *  # noqa
from fabvenv import virtualenv


def staging():
    env.hosts = ['ecobasa@server.sinnwerkstatt.com']
    env.path = '/srv/ecobasa.sinnwerkstatt.com/ecobasa/'
    env.virtualenv_path = '/srv/ecobasa.sinnwerkstatt.com/ecobasaenv/'
    env.push_branch = 'community-tours_goes_ecobasa'
    env.push_remote = 'github'


def production():
    env.hosts = ['m1487@ecobasa.org']
    env.path = '~/ecobasa/'
    env.virtualenv_path = '~/ecobasaenv/'
    env.push_branch = 'master'
    env.push_remote = 'origin'


def update():
    with cd(env.path):
        run("git pull %(push_remote)s %(push_branch)s" % env)
        with virtualenv(env.virtualenv_path):
            run("pip install -r requirements.txt")
            run("./manage.py collectstatic --noinput")
            run("cd ecobasa && django-admin.py compilemessages")


def migrate():
    with virtualenv(env.virtualenv_path):
        run("%(path)s/manage.py syncdb" % env)
        run("%(path)s/manage.py migrate" % env)


def reload():
    if env.tasks[0] == 'production':
        run("touch %(path)s/ecobasa/wsgi.py" % env)
    else:
        run("supervisorctl reload ecobasa")

def deploy():
    update()
    migrate()
    reload()
