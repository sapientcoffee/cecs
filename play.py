#! /usr/bin/env python

#==============================================================================
# Title:
# Description:
#
# Author:          		Rob Edwards (robedwa)
# Date:
# Version:
# Dependencies:
# Limitations/issues:
#==============================================================================
import requests
import json
import cecs
from prettytable import PrettyTable

import sys
from pprint import pprint


#
# Bash colours, for more see http://misc.flogisoft.com/bash/tip_colors_and_formatting
#
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


# if __name__ == '__main__':


    # from argparse import ArgumentParser, FileType
    #
    # p = ArgumentParser()
    # p.add_argument('srnumber',                          # Name stored in namespace
    #                metavar = 'Service Request Number',            # Arguement name displayed to user
    #                help = 'The Service Request return details of.',
    #                type = str
    #                 )

    #ns = p.parse_args()

#sr = cecs.report_tabular("", "sr-active")
    #sr = cecs.sr_details(ns.srnumber)
#srget = cecs.sr_get()

#pprint(sr)
    #pprint ("-----------------------------")
#pprint (srget)

#apioperation = "userAPIGetServiceRequests"
#r = cecs.ucsdCall(apioperation)
#pprint(r)

#call = cecs.VMNameToID('vm-Demo-SR465')

#r = json.loads(call.text)

#print call['VM_ID']
#print(call)

#j = json.dumps(call)
#print (call[0]['VM_ID'])
#print j

#pprint call['VM_Name']['VM_ID']
################################################################################

##
### Testing power VM on and off
##
# vm = "vm-Demo-SR465"
# action = "powerOn"
# comment = "testing API and python script"
#
# call = cecs.vm_action(vm, action, comment)
# print(call)

##
### SR Testing testing
##

# pprint(cecs.sr_get())
#
# srnumber = "467"
# pprint(cecs.sr_details(srnumber))
#
# pprint(cecs.sr_log(srnumber, ""))

##
###
##

# pprint(cecs.group_name('Demo'))

##
### Get all VMs and put in a table (including colours for the power status)

def list_vms(env):
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


print(list_vms("icfb"))
print(list_vms("ucsd"))




#print(table)

                              #
                            #   {u'Category': u'App Category 0',
                            #    u'Cloud': u'prov2',
                            #    u'Description': u' ',
                            #    u'Domain_Name': u'cisco.com',
                            #    u'Enterprise_IP': u'10.10.20.189 ',
                            #    u'Image_Id': u'',
                            #    u'Instance_ID': u'EILPC7ICF',
                            #    u'OS': u'RHEL 6.2 (64bit)',
                            #    u'Power_State': u'ON',
                            #    u'Provider_IP': u'N/A',
                            #    u'Tunnel_Status': u'up',
                            #    u'VM_ID': 207,
                            #    u'VM_Label': u'',
                            #    u'vDC': u'CiscoCloudVDC'}]}}




##
### Service Request Related
## Get all service requests

# sr = cecs.sr_get()
# all_sr = sr['serviceResult']['rows']
#
# srtable = PrettyTable(["ID", "Workflow", "Group/User", "Time", "Status"])
# srtable.align["ID"] = "l" # Left align
# srtable.padding_width = 1 # One space between column edges and contents (default)
#
# for item in all_sr:
#     a = item["Service_Request_Id"]
#     b = item["Catalog_Workflow_Name"]
#     if item["Group"] == "":
#         c = item["Initiating_User"]
#     else:
#         c = item["Group"] + "/" + item["Initiating_User"]
#     d = item["Request_Time"]
#     if item["Request_Status"] == "Complete":
#         e = GREEN + item["Request_Status"] + DEFAULT
#     elif item["Request_Status"] == "Failed":
#         e = RED + item["Request_Status"] + DEFAULT
#     else:
#         e = BLUE + item["Request_Status"] + DEFAULT
#
#     srtable.add_row([a, b, c, d, e])
#
# print(srtable)

## Get service requests details

# srdet = cecs.sr_details("476")
#
# pprint(srdet)

# stepId
# executionStatus (colour code stepId)

# u'serviceResult': {u'adminStatus': 1,
#                     u'cancelledByUser': None,
#                     u'cancelledTime': -1,
#                     u'entries': [{u'completedTime': 1443448868604,
#                                   u'executionStatus': 3,
#                                   u'handlerId': 4,
#                                   u'startAfter': -1,
#                                   u'startedTime': -1,
#                                   u'statusMessage': None,
#                                   u'stepId': u'Initiated by user',
#                                   u'validTill': -1},
#                                  {u'completedTime': 1443448876027,
#                                   u'executionStatus': 3,
#                                   u'handlerId': 12,
#                                   u'startAfter': -1,
#                                   u'startedTime': -1,
#                                   u'statusMessage': u'',
#                                   u'stepId': u'Create three tier component names',
#                                   u'validTill': -1},


#srlog = cecs.sr_log("476", "")
#pprint(srlog)
