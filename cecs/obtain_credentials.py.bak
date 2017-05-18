#! /usr/bin/env python

#==============================================================================
# Title:                obtain_credentials.py
# Description:          Will setup the local config file used by CECS module.
#
# Author:          		Rob Edwards (@clijockey)
# Date:                 28th November 2015
# Version:              0.1
# Dependencies:         configobj module
#                       cecs module
# Limitations/issues:
#==============================================================================

import sys
import os
import cecs
from configobj import ConfigObj
from os.path import expanduser

home = expanduser('~')
filename = home + '/.cecs.cfg'
# settings = home + filename

config = ConfigObj()
config.filename = filename

def query_yes_no(question, default="no"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def collect_settings(system):

    if system == 'ucsd':
        host = raw_input('What is the UCS Director hostname or IP : ')
    elif system == 'icfb':
        host = raw_input('What is the Intercloud Fabric Director hostname or IP : ')
    else:
        return "Inccorect system param passed, must be ucsd or icfb!"

    qu = query_yes_no("Do you already have your API key? ")
    if qu is True:
        apikey = raw_input('Brilliant, what is your API Key then? : ')
    elif qu is False:
        print('OK then, lets obtain it for you.')
        raw_input('What\'s your username : ')
        os.system("stty -echo")
        password = raw_input('What\'s your password :')
        os.system("stty echo")
        print "\n"

        apikey = "Getting key"
    else:
        print('something has gone wrong somewhere!!!')

    settings = {
        'hostname': host,
        'apikey': apikey,
    }
    return settings


config['UCSD'] = collect_settings('ucsd')
config['ICFB'] = collect_settings('icfb')
config.write()

try:
    with open(filename) as file:
        file_output = file.read()
        pass
except IOError as e:
    print "Unable to open file" #Does not exist OR no read permissions

print('Your settings file has been updated. Should things change you can edit directly at ' + filename + ' or you could just run this script again.\n')
print('You configuration file looks like this; \n' + file_output + '\n')
