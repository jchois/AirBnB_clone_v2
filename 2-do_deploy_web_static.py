#!/usr/bin/python3
"""Deploy archive"""
from fabric.contrib import files
from fabric.api import env, put, run
import os

env.hosts = ['34.75.8.225', '54.91.28.2']


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current'.format(name))
        run('ln -s {} /data/web_static/current'.format(dest))
        return True
    except:
        return False