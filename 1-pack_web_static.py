#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of
# the web_static folder of your AirBnB Clone repo,
# using the function do_pack

import os.path
from datetime import datetime
from fabric.api import *


@runs_once
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
