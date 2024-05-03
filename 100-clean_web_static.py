#!/usr/bin/python3
# that deletes out-of-date archives, using the function do_clean

import os
from datetime import datetime
from fabric.api import *


env.hosts = ['100.25.223.113', '52.91.183.15']


def do_clean(number=0):
    """deletes out-of-date archives
    If number is 0 or 1, keep only the most recent version of your archive.
    if number is 2, keep the most recent,
    and second most recent versions of your archive. etc."""
    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    start = int(number)
    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []
    for archive in archives:
        os.unlink('versions/{}'.format(archive))
    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    ]
    run(''.join(cmd_parts))
