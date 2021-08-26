#!/usr/bin/python3
"""Module that deploys the contents of web_static to the server"""
from fabric.api import local, hosts, put, run, env, runs_once

env.hosts = ['34.75.153.110', '18.208.193.84']


@runs_once
def do_pack():
    """Packs contents of web_static as a .tgz and returns its filepath."""
    from os import mkdir, path
    from datetime import datetime

    now = datetime.now()
    filename = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    filepath = "versions/{}".format(filename)

    try:
        mkdir('./versions')
    except FileExistsError:
        pass

    print("Packing web_static to {}".format(filepath))
    cmd = local('tar -cvzf {} web_static'.format(filepath))
    if (cmd.return_code == 0):
        filesize = path.getsize(filepath)
        print("web_static packed: {} -> {}Bytes".format(filepath, filesize))
        return filepath
    return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    from os import path

    if not path.exists(archive_path):
        print("No archive path given!")
        return False

    filename = archive_path.split('/')[1]
    dest_path = "/data/web_static/releases/{}/".format(filename.split('.')[0])

    try:
        print("Executing task do_deploy")
        put(archive_path, "/tmp/{}".format(filename))
        run('mkdir -p {}'.format(dest_path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, dest_path))
        run('rm /tmp/{}'.format(filename))
        run('mv {}web_static/* {}'.format(dest_path, dest_path))
        run('rm -rf {}web_static'.format(dest_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
