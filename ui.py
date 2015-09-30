#!/usr/bin/env python

#===============================================================================
# Title:                ui.py
# Description:          This is a menu based CLI tool using the UCSD/ICFD API.
#
# Author:          		Rob Edwards (robedwa)
# Date Updated:         30th September 2015
# Version:              0.5
# Dependencies:
# Limitations/issues:   This is far from being efficient python code. For a
#                       number or reasons it is how it is (for the time being)!
#===============================================================================

import sys, os
import json
import cecs
from prettytable import PrettyTable
from pprint import pprint

# Bash colours, for more see http://misc.flogisoft.com/bash/tip_colors_and_formatting
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
GREY = '\033[90m'
BLACK = '\033[90m'
DEFAULT = '\033[39m'

# Main definition - constants
#main_menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================
def common_options():
    print "m. Main"
    print "q. Quit"
    choice = raw_input(" Option >>  ")
    main_exec_menu(choice)
    return

def main_menu():
    os.system('clear')
    print "Welcome, this is an example of using the API for UCS Director and Intercloud Fabric Director\n"
    print "Please choose the menu you want to start:"
    print "1. Catalog Items"
    print "2. Service Requests"
    print "3. Infrastructure"
    #print "4. Consuption"
    print "\nq. Quit"
    choice = raw_input(" >>  ")
    main_exec_menu(choice)
    return

#################### Catalog Menu ##############################################
def catalog_menu():
    print("Catalog Menu (not implemented yet)!\n")
    common_options()
    #print "b. Back"
    #print "q. Quit"
    #choice = raw_input(" Catalog >>  ")
    #exec_menu(choice)
    #return

#################### Service Request Menu ######################################
def requests_menu():
    print "Requests Menu!\n"
    print "1. List all service requests"
    print "\nm. Main Menu"
    print "q. Quit"
    choice = raw_input(" Requests >>  ")
    requests_exec_menu(choice)
    #common_options()
    return

def request_list():
    print("All Service Requests!\n")
    # sr = cecs.sr_get()
    # print(sr)
    sr = cecs.sr_get()
    all_sr = sr['serviceResult']['rows']

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
            e = GREEN + item["Request_Status"] + DEFAULT
        elif item["Request_Status"] == "Failed":
            e = RED + item["Request_Status"] + DEFAULT
        else:
            e = BLUE + item["Request_Status"] + DEFAULT

        srtable.add_row([a, b, c, d, e])
    print(srtable)
    print("\nb. Back")
    print("q. Quit")
    choice = raw_input(" Requests >>  ")
    requests_exec_menu(choice)
    return
    #common_options()
    # choice = raw_input(" Requests >>  ")
    # requests_exec_menu(choice)
    # return

#################### Infrastructure Menu #######################################
def infra_menu():
    print("Infrastructure Menu!\n")
    print("1. List UCSD Virtual Machines")
    print("2. List ICFB Virtual Machines")
    print "\n m. Main Menu"
    print "q. Quit"
    choice = raw_input(" Option >>  ")
    infra_exec_menu(choice)
    return

def vm_list(env):
    j = cecs.getAllVMs(env)
    all_vms = j['serviceResult']['rows']

    table = PrettyTable(["ID", "Name", "IP Address(s)", "Power", "VDC"])
    table.align["Name"] = "l" # Left align
    table.padding_width = 1 # One space between column edges and contents (default)

    for item in all_vms:
        # Values that are the same for UCSD & ICFB responses
        a = item["VM_ID"]
        if item["Power_State"] == "ON":
            d = GREEN + item["Power_State"] + DEFAULT
        elif item["Power_State"] == "OFF":
            d = RED + item["Power_State"] + DEFAULT
        else:
            d = BLUE + item["Power_State"] + DEFAULT
        e = item["vDC"]

        # Values that differ between UCSD & ICFB
        if env == "ucsd":
            b = item["VM_Name"]
            c = item["IP_Address"]
        elif env == "icfb":
            b = item["Instance_ID"]
            c = item["Enterprise_IP"]

        table.add_row([a, b, c, d, e])
    return table

def vm_list_ucsd():
    print("Obtaining requested data (this may take a minute) .............")
    print("Please hold the line caller you are important to us.")
    print(vm_list("ucsd"))
    print("\nb. Back")
    print("q. Quit")
    choice = raw_input(" Infrastructure >>  ")
    infra_exec_menu(choice)
    return

def vm_list_icfb():
    print("Obtaining requested data (this may take a minute) .............")
    print("Please hold the line caller you are important to us.")
    print(vm_list("icfb"))
    print("b. Back")
    print("q. Quit")
    choice = raw_input(" Infrastructure >>  ")
    infra_exec_menu(choice)
    return
#################### Consuption/Billing Menu ###################################
def consumption_menu():
    print "Consuption Menu!\n"
    # print "b. Back"
    # print "q. Quit"
    # choice = raw_input(" Consumption >>  ")
    # exec_menu(choice)
    common_options()
    #return


# Back to main menu
# def back():
#     main_menu_actions['main_menu']()

# Exit program
def exit():
    print("Thank you for using, have a nice day!")
    sys.exit()

# ------------------------------------------------------------------------------
# Execute menu
def main_exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        main_menu_actions['main_menu']()
    else:
        try:
            main_menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            main_menu_actions['main_menu']()
    return

def requests_exec_menu(choice):
        os.system('clear')
        ch = choice.lower()
        if ch == '':
            requests_menu_actions['main_menu']()
        else:
            try:
                requests_menu_actions[ch]()
            except KeyError:
                print "Invalid selection, please try again.\n"
                requests_menu_actions['main_menu']()
        return

def infra_exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        infra_menu_actions['main_menu']()
    else:
        try:
            infra_menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            infra_menu_actions['main_menu']()
    return



# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
main_menu_actions = {
    'main_menu': main_menu,
    '1': catalog_menu,
    '2': requests_menu,
    '3': infra_menu,
    'm': main_menu,
    'q': exit,
}

requests_menu_actions = {
    'main_menu': requests_menu,
    '1': request_list,
    'm': main_menu,
    'b': requests_menu,
    'q': exit,
}

infra_menu_actions = {
    'main_menu': infra_menu,
    '1': vm_list_ucsd,
    '2': vm_list_icfb,
    'm': main_menu,
    'b': infra_menu,
    'q': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
