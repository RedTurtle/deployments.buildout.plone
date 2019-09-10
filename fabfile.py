"""
Commands available to deploy using rt.commands
"""
# this is necessary to make the fabric commands available
from fabric.api import env
from rt.commands import *
from rt.commands.project import *
from rt.commands.buildout_components import *

# This is the main python version
env.python_version = '3.7'

# This is the buildout script to use
env.buildout_cfg = 'buildout.cfg'

# And some hosts
env.staging_user = ''
env.staging_host = ''
env.staging_dir = ''
env.production_user = ''
env.production_host = ''
env.production_dir = ''
