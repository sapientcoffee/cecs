
'''
    Python module of different functions for manipulating UCS Director
    via the API.
'''
import requests
import json
#import os

from markdown import markdown
from pprint import pprint

# import standard variables and configuration info
from local_config import ucsdserver, ucsd_key, url, getstring, parameter_lead, headers, icfdserver, icfd_key
headers["X-Cloupia-Request-Key"] = icfd_key



#################### Core Functions ############################################
#    Python module of different functions for working with data.
#    These functions are used in the other libraries as utilities.
################################################################################

def dict_filter(source_dict, filter_list):
    '''
    For a given dictionary, return a new dictionary with only the keys included
    in the filter.  If the filter_list is empty, return entire source_dict
    :param source_dict:  The dictionary to filter key values for.
    :param filter_list:  A list of the key values you wish to maintain.
    :return:
    '''
    if (len(filter_list) == 0): return source_dict
    result = {key: source_dict[key] for key in filter_list}
    # print result
    return result

def list_search(list, result_filter):
    '''
    Filter down a given list of dictionaries for only those elements where there is
    a match for one of the key:value matches in the result_filter dictionary.
    If there are more than one entry in the result_filter, only one must match.
      (searching is an OR construct)
    If the result_filter is empty, return the whole list.
    :param list: The list of dictionaries to search over
    :param result_filter: A dictionary of values to search for
    :return:
    '''
    if (len(result_filter) == 0): return list
    new_list = []
    for l in list:
        for key in result_filter.keys():
            if (l[key] == result_filter[key]):
                new_list.append(l)
                break
    return new_list



def apiCall(api, param0 = None, param1 = None, param2 = None, param3 = None):
    '''
    Craetes the URL format to make the call to UCS Director Rest API.
    This is a hacked version of overloading (not sure how else to achieve)
    :param api: The specific API call required
    :param param0: The initial parameter required to create the request structure
    :return: JSON response from API call
    '''

    if param0 is None:
        u = url % (icfdserver) + getstring % (api) + parameter_lead + \
        "{}"
    elif param1 is None:
        u = url % (icfdserver) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '"' + '}'
    elif param2 is None:
        u = url % (icfdserver) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '",' + \
        ',param1:"' + param1 + '"}'
    elif param3 is None:
        u = url % (icfdserver) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '",' + \
        'param1:"' + param1 + '"' + \
        ',param2:"' + param2 + '"}'

    r = requests.get(u, headers=headers)
    j = json.loads(r.text)
    return j


####################  Intercloud Fabric ########################################
#                   Intercloud Fabric
#   These make use of the ICF API
################################################################################


def icf_GetAllVMs():
    '''
    Returns all VMs for the logged-in user.
    :param api: The specific API call required
    :return: APITabularReport
    '''
    apioperation = "Intercloud:userAPIGetAllVms"

    r = apiCall(apioperation)
    return r

def icf_GetVM():
    '''
    Returns details for the specified VM.
    :param api: The specific API call required
    :param param0: vmID—The VM identifier available from the VM report screen.
    :return: APITabularReport
    '''
    apioperation = "Intercloud:userAPIGetVMSummary"

    r = apiCall(apioperation)
    return r

def icf_MoveVM():
    '''
    Returns details for the specified VM.
    :param api: The specific API call required
    :param param0: vmID—The VM identifier available from the VM report screen.
    :return: APITabularReport
    '''
    apioperation = "ntercloud:userAPIMoveVMToCloud"

    r = apiCall(apioperation)
    return r

# def icf_GetVM():
#     '''
#     Returns details for the specified VM.
#     :param api: The specific API call required
#     :param param0: vmID—The VM identifier available from the VM report screen.
#     :return: APITabularReport
#     '''
#     apioperation = "Intercloud:userAPIGetVMSummary"
#
#     r = apiCall(apioperation)
#     return r
#
# def icf_GetVM():
#     '''
#     Returns details for the specified VM.
#     :param api: The specific API call required
#     :param param0: vmID—The VM identifier available from the VM report screen.
#     :return: APITabularReport
#     '''
#     apioperation = "Intercloud:userAPIGetVMSummary"
#
#     r = apiCall(apioperation)
#     return r

def operations(server, status):
    '''
    This will alter the status (on, off etc.) of a VM. It has to work out the
    vmid based on the VM name that is passed.
    '''

    #call a function to work out the server vmid based on name (this will need to be created)

    # if status == "off":
    #     apioperation = "Intercloud:userAPIVmPowerOff"
    # elif status == "on":
    #     apioperation = "Intercloud:userAPIVmPowerOn"
    # elif status == "reboot"
    #     apioperation = "Intercloud:userAPIVmReboot"
    # elif status = "terminate"
    #     apioperation = "Intercloud:userAPIVmTerminate"


    r = ucsdCall(apioperation, vmid)
#def migrate(server, location):
