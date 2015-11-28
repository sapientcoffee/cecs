#!/usr/bin/env python

#===============================================================================
# Title:                cecs-cli.py
# Description:
#
# Author:          		Rob Edwards (robedwa)
# Date Updated:         November 2015
# Version:              0.1
# Dependencies:
# Limitations/issues:   This is far from being efficient python code. For a
#                       number or reasons it is how it is (for the time being)!
#                       Spell check needs to take place!
#===============================================================================

import cecs
import click
from colorama import init
from colorama import Fore, Back, Style
from prettytable import PrettyTable

# Initialising the colorama module
init()

clientVersion = '0.1.dev1'

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    '''Cisco Enterprise Cloud Suite Command Line Interface.

    This is a CLI to interact with the compoenents of CECS.
    Initially this only works with UCS Director (UCSD) and
    Intercloud Fabric for Business (ICFB). As this project
    evolves other tools will be incorporated.

    \b
    UCS Director:

    UCSD is a data centre automation and orchestration tool.
    It manages on-premise network, storage and compute
    (physical & virtual).

    \b
    Intercloud Fabric:

    ICFB is hard of the Cisco hybrid cloud strategy that allows,
    you to extend your on-premise networks into provider and public
    clouds. It also provides the capabulities to migrate workloads
    between clouds taking care of any converstion processes.
    '''
    pass

@cli.command()
@click.option('--item', '-i', default='service-requests', help='Items you want ot list')
@click.option('--env', '-e', default='ucsd', help='Select the environment, either ucsd or icfb')
def list(env, item):
    ''' This will list a number of things managed by Cisco Enterprise Cloud Suite.

    Initially this will be UCS Dirctor only and will evolve to use ICFB
    '''
    click.echo('Listing various things')

    if (item == 'vm') or (item == 'virtual-machines'):
        click.echo('Listing virtual machines')
    elif (item == 'catalog'):
        click.echo('Listing catalog items')
    elif (item == 'service-requests') or (item == 'sr'):
        # Request the list of service request items from the env (i.e. ucsd or icfb)
        sr = cecs.sr_get(env)
        all_sr = sr['serviceResult']['rows']

        # Put the result into a nice table format
        srtable = PrettyTable(["ID", "Workflow", "Group/User", "Time", "Status"])
        srtable.align["ID"] = "l" # Left align
        srtable.padding_width = 1 # One space between column edges and contents (default)

        for item in all_sr:
            a = item["Service_Request_Id"]
            b = item["Catalog_Workflow_Name"]
            if item["Group"] == "":
                c = item["Initiating_User"]
            else:
                c = item["Group"] + "/" + item["Initiating_User"]
            d = item["Request_Time"]
            if item["Request_Status"] == "Complete":
                e = Fore.GREEN + item["Request_Status"] + Style.RESET_ALL
            elif item["Request_Status"] == "Failed":
                e = Fore.RED + item["Request_Status"] + Style.RESET_ALL
            else:
                e = Fore.CYAN + item["Request_Status"] + Style.RESET_ALL

            srtable.add_row([a, b, c, d, e])

        # Return the requsts in nice table format
        click.echo(srtable)

@cli.command()
def order():
    click.echo('Order stuff')

@cli.command()
def version():
    '''Client & server versions '''
    ucsdver = cecs.version('ucsd')
    icfbver = cecs.version('icfb')

    #click.echo('The version of both server and client')
    click.echo('-' * 60)
    click.echo(ucsdver)
    click.echo(icfbver)
    click.echo('Script version : ' + clientVersion)
    click.echo('-' * 60)

@cli.command()
def order():
    '''Order items '''
    click.echo('Alter the state of things (on, off, terminate)')

@cli.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    """This script works similar to the Unix `cat` command but it writes
    into a specific file (which could be the standard output as denoted by
    the ``-`` sign).
    \b
    Copy stdin to stdout:
        inout - -
    \b
    Copy foo.txt and bar.txt to stdout:
        inout foo.txt bar.txt -
    \b
    Write stdin into the file foo.txt
        inout - foo.txt
    """
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    cli()
