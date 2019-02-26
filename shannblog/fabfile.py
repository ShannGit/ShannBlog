from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = 'https://github.com/ShannGit/shann-blog.git'
env.user = 'T'
env.password = 'asd5560595'
env.hosts = ['47.94.217.141']
env.port = '22'

def deploy():
	source_folder = '/home/T/myproject/shannblog/shann-blog/shannblog'
	run('cd %s && git pull' % source_folder)
	run("""
		cd {} &&
		../../env/bin/pip3 install -r requirements.txt &&
		../../env/bin/python3 manage.py collectstatic --noinput &&
		../../env/bin/python3 manage.py migrate
		""".format(source_folder))
	sudo('systemctl start shannblog')
	sudo('service nginx reload')