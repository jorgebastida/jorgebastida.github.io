# encoding: utf-8
import re
from fabric.api import *

env.project_dir = '/home/jorgebastida.com.git'

def deploy():
    with cd(env.project_dir):
        run("git pull")