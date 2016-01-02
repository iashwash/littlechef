"""Cook with Chef without a Chef Server

With LittleChef you will be able to get started more quickly cooking with
Chef_, the excellent Configuration Management System.

You will just need your local (preferably version controled) kitchen with all
your cookbooks, roles data bags and nodes, which will get rsynced to a node
each time you start a Chef Solo configuration run with the bundled 'fix'
command.

It also adds features to Chef Solo that are currently only available for Chef
Server users: data bag search, and node search.

.. _Chef: http://wiki.opscode.com/display/chef/Home

"""
import os
__version__ = "1.8.0"
__author__ = "Miquel Torres <tobami@gmail.com>"

__cooking__ = False

chef_environment = None
kitchen_path = os.getcwd()

loglevel = "info"
noninteractive = False
verbose = False
enable_logs = True
LOGFILE = "/var/log/chef/solo.log"
whyrun = False
concurrency = False
include_guests = False
skip_node_data_bag = False
no_color = False

node_work_path = "/tmp/chef-solo"
cookbook_paths = ['site-cookbooks', 'cookbooks']

CONFIGFILE = "littlechef.cfg"
