#!/usr/bin/python3
"""
generate a .tgz achive from the contents of web_static website
usage:
  fab -f 1-pack_web_static.py do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates .tgz archive from the contents of /web_static
       returns archive's path if successful and None if not
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    filepath = 'versions/web_static_{}.tgz'.format(now)

    local('mkdir -p versions/')
    createArchive = local('tar -cvzf {} web_static/'.format(filepath))

    if createArchive.succeeded:
        return filepath
