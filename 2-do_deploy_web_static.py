#!/usr/bin/python3
# distributes an archive to your web servers, using the function do_deploy

import os.path
from datetime import datetime
from fabric.api import *


env.hosts = ['100.25.223.113', '52.91.183.15']


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if os.path.exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    # so now filename is <web_static_2021041409349.tgz>
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
        print('New version deployed!')
        return True
    except:
        return False
