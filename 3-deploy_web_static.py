#!/usr/bin/python3
# creates and distributes an archive to your web servers,
# using the function deploy

import os.path
from datetime import datetime
from fabric.api import *


env.hosts = ['100.25.223.113', '52.91.183.15']


def do_pack():
    """ Fabric script that generates a .tgz archive """
    local("sudo mkdir -p versions")
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(time_now)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if os.path.exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    no_tar = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = '/tmp/' + filename

    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}/".format(no_tar))
        run('tar -xzf {} -C {}'.format(tmp, no_tar))
        run('rm {}'.format(tmp))
        run('mv {}/web_static/* {}'.format(no_tar, no_tar))
        run('rm -rf {}/web_static'.format(no_tar))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(no_tar))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    file_name = do_pack()
    if os.path.exists(file_name) is False:
        return False
    return do_deploy(file_name)
