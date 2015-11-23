#! /usr/bin/env python

#==============================================================================
# Title:                cecs
# Description:          This is a module to assist with the interaction both the
#                       UCSD & ICFB APIs for other Pyton scripts.
#
# Author:          		Rob Edwards (robedwa)
# Date:                 30/09/15
# Version:              0.1.10
# Dependencies:
# Limitations/issues:   Early days of the module
#==============================================================================
'''
    Python module of different functions for manipulating UCS Director
    via the API.
'''
import requests
import json

from markdown import markdown
#from pprint import pprint

# import standard variables and configuration info
from local_config import ucsdserver, ucsd_key, url, getstring, parameter_lead, headers, icfbserver, icfb_key
# headers["X-Cloupia-Request-Key"] = ucsd_key

# Being lazy and avoiding checking the SSL cert and as a result want to hide the erros associated :)
requests.packages.urllib3.disable_warnings()

#################### Core Functions ############################################
#    Python module of different functions for working with data.
#    These functions are used in the other libraries as utilities.
################################################################################

# def dict_filter(source_dict, filter_list):
#     '''
#     For a given dictionary, return a new dictionary with only the keys included
#     in the filter.  If the filter_list is empty, return entire source_dict
#     :param source_dict:  The dictionary to filter key values for.
#     :param filter_list:  A list of the key values you wish to maintain.
#     :return:
#     '''
#     if (len(filter_list) == 0): return source_dict
#     result = {key: source_dict[key] for key in filter_list}
#     # print result
#     return result
#
# def list_search(list, result_filter):
#     '''
#     Filter down a given list of dictionaries for only those elements where there is
#     a match for one of the key:value matches in the result_filter dictionary.
#     If there are more than one entry in the result_filter, only one must match.
#       (searching is an OR construct)
#     If the result_filter is empty, return the whole list.
#     :param list: The list of dictionaries to search over
#     :param result_filter: A dictionary of values to search for
#     :return:
#     '''
#     if (len(result_filter) == 0): return list
#     new_list = []
#     for l in list:
#         for key in result_filter.keys():
#             if (l[key] == result_filter[key]):
#                 new_list.append(l)
#                 break
#     return new_list

def ucsdCall(api, param0 = None, param1 = None, param2 = None, param3 = None, param4 = None):
    '''
    NOTE: This is deprecated and will be removed once all functions have been migrated!

    Craetes the URL format to make the call to UCS Director Rest API.
    This is a hacked version of overloading (not sure how else to achieve)
    :param api: The specific API call required
    :param param0: The initial parameter required to create the request structure
    :return: JSON response (in Python dictionary) from API call
    '''
    headers["X-Cloupia-Request-Key"] = ucsd_key
    if param0 is None:
        u = url % (ucsdserver) + getstring % (api) + parameter_lead + \
        "{}"
    elif param1 is None:
        u = url % (ucsdserver) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '"' + '}'
    elif param2 is None:
        u = url % (ucsdserver) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '",' + \
        ',param1:"' + param1 + '"}'
    elif param3 is None:
        u = url % (ucsdserver) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '",' + \
        'param1:"' + param1 + '"' + \
        ',param2:"' + param2 + '"}'
    elif param4 is None:
        u = url % (ucsdserver) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '",' + \
        'param1:"' + param1 + '"' + \
        'param2:"' + param2 + '"' + \
        ',param3:"' + param3 + '"}'

    r = requests.get(u, headers=headers)
    j = json.loads(r.text)
    return r

def apiCall(env, api, param0 = None, param1 = None, param2 = None, param3 = None, param4 = None):
    '''
    Craetes the URL format to make the call to UCS Director or Intercloud Fabric
    Rest API. This is a hacked way to achieve overloading
    :param env: Specify if the API call should be against UCSD or ICFB
    :param api: The specific API call required
    :param param0: The initial parameter required to create the request structure
    :param param1: The 2nd if required
    :param param2: The 3rd if required
    :return: JSON response from API call
    '''

    if env == 'icfb':
        headers["X-Cloupia-Request-Key"] = icfb_key
        server = icfbserver
    elif env == 'ucsd':
        headers["X-Cloupia-Request-Key"] = ucsd_key
        server = ucsdserver

    if param0 is None:
        u = url % (server) + getstring % (api) + parameter_lead + \
        "{}"
    elif param1 is None:
        u = url % (server) + getstring % (api) + parameter_lead + \
        "{param0:" + param0 + '}'
    elif param2 is None:
        u = url % (server) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '",' + \
        ',param1:"' + param1 + '"}'
    elif param3 is None:
        u = url % (server) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '",' + \
        'param1:"' + param1 + '"' + \
        ',param2:"' + param2 + '"}'
    elif param4 is None:
        u = url % (server) + getstring % (api) + parameter_lead + \
        "{param0:\"" + param0 + '",' + \
        'param1:"' + param1 + '"' + \
        'param2:"' + param2 + '"' + \
        ',param3:"' + param3 + '"}'

    # Due to the setup of the lab I have disabled the SSL cert verification however
    # in a production environemnt I would sugest changing verify to True so that the
    # SSL certs are validated!!
    print u
    r = requests.get(u, headers=headers, verify=False)
    j = json.loads(r.text)
    return j

#################### VM Operations #############################################
#L G UserAPIProvisionRequest                Provisions a virtual machine (VM).
#L G UserAPIProvisionRequestWithPortGroup   Provisions a VMWare VM and allows a user to select the port group name while provisioning a VM
#    userAPIGetAllVMs                       Returns all VMs for the logged-in user. No parameters are required.
#    userAPIGetVMSummary                    Returns a summary of a specified VM.
#  userAPIGetVMsForServiceRequest           Returns VMs that are currently associated with the specified service request.
# userAPIGetVMActionRequests                Returns VM Action requests for a given context.
# userAPIGetAvailableVMActions              Returns the available VM Actions for a given VM ID
# userAPIExecuteVMAction (for Generic VMs)  Executes a specific Power Management Option action on a given generic VM.
# userAPIExecuteVMAction (for VMware vSphere VMs)   Executes a specific Power Management Option action on a given VMware vSphere VM.
# userAPIExecuteVMAction (for Microsoft Hyper-V VMs)    Executes a specific Power Management Option action on a given Microsoft Hyper-V VM.
# userAPIHypervVMProvisioningWithVMNetwork  Provisions a Hyper-V VM that is associated with the network group
# userAPIReconfigureVM                      Resizes the specified VM.
# userAPIGetVMActionStatus                  Returns the VM Action Status for a given VM Action Request.
# userAPISetVMProperties                    Assigns a user label to a VM.
# userAPIGetVMAccessCredentials             Returns VM access credentials.
# userAPIGetVMSnapshotDetails               Returns VM snapshot details.
# userAPICreateVMSnapshot                   Creates a snapshot based on the parameters provided. The snapshot is a backup of existing data on VM. An end user can later restore to a snapshot in case of a VM failure.
# userAPICheckContextActionStatus           Returns the status message details of the VM action
# userAPIDeleteCatalogItem                  Deletes the catalog that is created for provisioning a VM
# userAPIVMWareProvisionRequest             Provisions a VMware VM using a template and returns the service request (SR) ID as an integer value
# userAPIVMWareCloneVMProvisionRequest      Clones a VMware VM and returns the service request (SR) ID as an integer value
# userAPIVMWareMoveVMProvisionRequest       Moves a VM to vDC and returns the service request (SR) ID as an integer value
# userAPIConfigureVMLeaseTime               Configures a lease expiration time for a selected VM. Once the lease time expires, the VM is shutdown (powered-off)
################################################################################

#def req_provision():
    # /app/api/rest?formatType=json&opName=userAPIProvisionRequest&opData={param0:{"catalogName":"sample","vdcName":"sample","userID":"sample","durationHours":1000,"beginTime":0,"quantity":1000,"memoryMB":0,"diskGB":1000,"cores":1000,"estimatedCost":1000.0,"comments":"sample","additionalInfo":"sample","chargeFrequency":1000,"nicAliasName":"sample","nicPortGroupName":"sample","resourceAllocated":true,"allocatedHost":"sample","allocatedDataStore":"sample","allocatedResourcePool":"sample","altAllocatedHost":"sample","altAllocatedDataStore":"sample","altAllocatedResourcePool":"sample","customStartupMemory":1000.0,"customMaxMemory":1000.0,"customMemoryBuffer":1000.0,"customMemoryConfig":true,"customStoragePolicy":"sample","allocatedCluster":"sample","customCpuSockets":1000,"customCpuCoresPerSocket":1000,"altAllocatedCluster":"sample","allocatedAddnlDatastores":"sample","altAllocatedAddnlDatastores":"sample","altAllocatedAddnlVNICs":"sample","altAllocatedAddnlVNICsIpv6":"sample","selectedDiskDataStore":"sample","actionId":"sample","vmName":"sample","vdcCategory":"sample","windowsLicensePool":"sample","templateUserId":"sample","templatePassword":"sample","credentialOption":"sample","provisionAllDisk":true,"enableGuestCustomization":true,"enablePostProvisioningCustomActions":true,"workflow":"sample","vmId":1000,"vMAppChargeFrequency":1000,"activeVMAppCost":1000.0,"inactiveVMAppCost":1000.0,"useLinkedClone":true,"snapshotId":1000,"snapshotKey":"sample","newSnapshotName":"sample","isHighlyAvailable":true,"postProvWFUserInputs":{"list":[{"name":"sample","value":"sample"},{"name":"sample","value":"sample"}]}}}
    #Following parameters are mandatory for provisioning a VM:
    #   String catalogName
    #   String vdcName
    #   String userID

#################### Workflow Operations #######################################
# This section contains the 'Workflow Operations' calls. Based on version 5.3.
#
#    + userAPIGetWorkflows					Returns the workflows in a folder.
#    + userAPIGetWorkflowSteps              Returns the steps involved in the specified workflow.
#    + userAPIGetWorkflowStatus				Returns the execution status code of a workflow.
#    + userAPIGetWorkflowInputs				Returns the inputs of a workflow
#    - userAPIValidateWorkFlow				Validates the workflow and returns the result.
#    userAPISubmitWorkflowServiceRequest	Submits a service request with a workflow. Returns the ID of the service request.
#    + userAPIRollbackWorkflow				Rolls back the specified service request ID.
#    userAPIExportWorkflows					Exports the specified workflows.
#    userAPIImportWorkflows					Imports the workflow into the system.
################################################################################

# def workflow_list(folder = "", key_filter = [], result_filter = {}):
#     '''
#     Query UCS Director for the workflows of a folder
#     :param folder: The UCSD Orchestration Folder to Query - defaults to all
#     :return:
#     '''
#     apioperation = "userAPIGetWorkflows"
#     u = url % (ucsdserver) + getstring % (apioperation) + parameter_lead + \
#     "{param0:\"" + folder + '"' + '}'
#
#     r = requests.get(u, headers=headers)
#     j = json.loads(r.text)
#
#     j['serviceResult'] = list_search(j['serviceResult'], result_filter)
#
#     search_results = [dict_filter(r, key_filter) for r in j['serviceResult']]
#     return search_results
#
# def workflow_steps(srnumber):
#         '''
#         Query UCS Director for the steps involved in a service requet workflow
#         :param srnumber: The service request ID
#         :return: List <APIWorkflowStep>
#         '''
#         apioperation = "servicerequest:userAPIGetWorkflowSteps"
#         u = url % (ucsdserver) + getstring % (apioperation) + parameter_lead + \
#         "{param0:{\"requestId\":" + srnumber + "}}"
#
#         r = requests.get(u, headers=headers)
#
#         return r.text
#
# def workflow_inputs(workflow):
#     '''
#     Query UCS Director for the inputs for a workflow
#     :param workflow: The workflow name to lookup inputs for
#     :return:
#     '''
#     apioperation = "userAPIGetWorkflowInputs"
#     u = url % (ucsdserver) + getstring % (apioperation) + parameter_lead + \
#     "{param0:\"" + workflow + '"' + '}'
#
#     r = requests.get(u, headers=headers)
#     j = json.loads(r.text)
#
#     return j['serviceResult']['details']
#
# # Need to validate and check - written when on plane and no access to test
# def workflow_validate(workflow):
#     '''
#     Validate UCS Director workflow
#     :param workflow: The workflow name to lookup inputs for
#     :return: Result
#     '''
#     param0 = workflow
#
#     apioperation = "userAPIValidateWorkFlow"
#     u = url % (ucsdserver) + getstring % (apioperation) + parameter_lead + \
#     "{param0:\"" + workflow + '"' + '}'
#
#     #r = requests.get(u, headers=headers)
#     #j = json.loads(r.text)
#
# def workflow_execute(workflow, inputs):
#     '''
#     Create a Service Request based on the specified Workflow and with Inputs.
#     :param workflow:    The workflow name to execute
#     :param inputs:      dict of inputs with Input Label as Key
#     :return:            JSON of the Service Request Created
#     '''
#     param0 = workflow
#
#     # Get the workflow inputs
#     wf_inputs = workflow_inputs(workflow)
#
#     param1 = [{"name": i['label'], "value":inputs[i['label']]} for i in wf_inputs]
#     param2 = "-1"
#
#     apioperation = "userAPISubmitWorkflowServiceRequest"
#     u = url % (ucsdserver) + getstring % (apioperation) + parameter_lead + \
#     "{param0:\"" + param0 + '",' + \
#     'param1:{"list":' + json.dumps(param1) + '}' + \
#     ',param2:' + param2 + '}'
#
#     r = requests.get(u, headers=headers)
#
#     j = json.loads(r.text)
#
#     return j
#
# def sr_rollback(srnumber):
#     '''
#     Rollback the Service Request Specified
#     :param srnumber: The Service Request ID
#     :return: JSON status of the request
#     '''
#     apioperation = "userAPIRollbackWorkflow"
#     u = url % (ucsdserver) + getstring % (apioperation) + parameter_lead + \
#     "{param0:\"" + srnumber + '"' + '}'
#
#     r = requests.get(u, headers=headers)
#
#     return r.text
#
# # Need to validate and check - written when on plane and no access to test
# def workflow_export():
#     '''
#     Export UCS Director workflow
#     :param workflow: The workflow name to lookup inputs for
#     :return:
#     '''
#     #insert check to see if the user has admin priv? Infact check what happens if none admin tries to run it!
#
#     apioperation = "userAPIExportWorkflows"

#################### Service Request Operations #################################
# This section contains the 'Service Request Operations' calls. Based on version 5.3.
#
#L G  userAPISubmitServiceRequest			    [DEPRICATED] Submits a service request for provisioning VMs. Supports Qty 1. Replaced with userAPIProvisionRequest
#L G  userAPISubmitServiceRequestCustom         [DEPRICATED] Submits a service request for provisioning virtual machines (VMs) with the inputs vmName, vCPU, and memory.
#L G  userAPIResubmitServiceRequest             Resubmits a service request for processing the specified service request.
#L G  + userAPIGetServiceRequests	            Returns all service requests for the user
#L G  userAPIGetChildServiceRequests            Returns the child service requests of the specified parent service request.
#L G  userAPIGetServiceRequestDetails           Returns service request details.
#L G userAPICancelServiceRequest				Cancels a service request in progress.
#L G + userAPIGetServiceRequestLogEntries		Returns the log entries of a service request for the requested severity
#L G userAPIGetServiceRequestLogEntriesAtLevels	Returns the log entries of a service request for the requested severity
#L G + userAPIGetServiceRequestWorkFlow		    Returns service request workflow details.
#L G userAPISubmitVAppServiceRequest			Submits a service request with the virtual application catalog type and arguments.
#L G + userAPIGetVMsForServiceRequest			Returns VMs that are currently associated with the specified service request.
#L G userAPISubmitWorkflowServiceRequest		Submits a service request with a workflow. Returns the ID of the service request.
#
#
################################################################################

def sr_get(env):
    '''
    Return the service request for the logged in user (Both UCSD & ICFB)
    :return: APITabularReport (JSON)
    '''
    apioperation = "userAPIGetServiceRequests"
    r = apiCall(env, apioperation)
    #j = json.loads(r.text)
    return r

def sr_details(srnumber):
    '''
    Return the details of the Service Request Specified - Workflow Based Only
    :param srnumber: The Service Request ID
    :return: JSON of the SR Status
    '''
    apioperation = "userAPIGetServiceRequestWorkFlow"
    r = ucsdCall(apioperation, srnumber)
    return r

def sr_log(srnumber, severity):
    '''
    Return the logs from the specified Service Request
    :param srnumber: The Service Request ID
    :param severity: Log severity (debug, info, warning, error)
    :return: JSON of the logs
    '''
    apioperation = "userAPIGetServiceRequestLogEntries"

    if severity == 'debug':
        severity = '0'
    elif severity == 'info':
        severity = '1'
    elif severity == 'warning':
        severity = '2'
    elif severity == 'error':
        severity = '3'
    else:
        severity = '1000'

    r = ucsdCall(apioperation, srnumber, severity)
    return r

# def sr_vms(srnumber):
#     '''
#     Return the VMs of the Service Request Specified
#     :param srnumber: The Service Request ID
#     :return: JSON of the SR Status
#     '''
#     apioperation = "userAPIGetVMsForServiceRequest"
#     u = url % (ucsdserver) + getstring % (apioperation) + parameter_lead + \
#     "{param0:\"" + srnumber + '"' + '}'
#
#     r = requests.get(u, headers=headers)
#     j = json.loads(r.text)
#
#     return j['serviceResult']['vms']



def group_name(name):
    apioperation = "userAPIGetGroupByName"
    r = ucsdCall(apioperation, name)
    return r

#################### Reports ###################################################
def report_tabular(group, report):
    #'''
    # Old v1 of the API, although userAPIGetServiceRequests will get only for logged in user. If using SERVICE-REQUESTS-T10 get get all.
    #'''
    apioperation = "userAPIGetTabularReport"

    if group == "":
        rptid = "6"
        grpid = ""
    else:
        rptid = "7"
        grp = group_name(group)
        grpid = str(grp['serviceResult'][0]['groupId'])

    if report == 'sr-active':
        r = ucsdCall(apioperation, rptid, grpid, "SERVICE-REQUESTS-T10" )
        return r
    elif report == 'sr-archive':
        r = ucsdCall(apioperation, rptId, grpid, "ARCHIVED-SERVICE-REQUESTS-T10" )
        return r




####################  Working On ###############################################
#                   WORKING ON
################################################################################

def getAllVMs(env):

    if env == "ucsd":
        apioperation = "userAPIGetAllVMs"
    elif env == "icfb":
        apioperation = "Intercloud:userAPIGetAllVms"

    #apioperation = "Intercloud:userAPIGetAllVMs"
    #apioperation = "userAPIGetAllVMs"
    #env = "ucsd"
    print("About to call in getAllVMs " + env + " using " + apioperation )
    r = apiCall(env, apioperation)
    #r = ucsdCall(apioperation)
    #j = json.loads(r.text)

    return r

def VMNameToID(env, vm_name):
    '''
    Will return the 'vmid' when the VM Name is passed. Currently on UCSD but will be expanded to ICF
    :param api: The specific API call required
    :param: VM_Name
    :return: vmid
    '''
    if env == "ucsd":
        apioperation = "userAPIGetAllVMs"
    elif env == "icfb":
        apioperation = "Intercloud:userAPIGetAllVms"

    print("About to call in VMnameToID " + env + " using " + apioperation)
    r = apiCall(env, apioperation)

    all_vms = r['serviceResult']['rows']
    if env == "ucsd":
        print("Checking against UCSD")
        for vm in all_vms:
            if (vm['VM_Name'] == vm_name):
                vmid = vm['VM_ID']
                return vmid
            else:
                vmid = "Error, " + vm_name + " not found!!"
    elif env == "icfb":
        print("Checking against ICFB")
        for vm in all_vms:
            if vm['Instance_ID'] == vm_name:
                vmid = vm['VM_ID']
                return vmid
            else:
                vmid = "Error, " + vm_name + " not found!!"

def vm_action(env, vm_name, action, comment):
    '''
    This will alter the status (on, off etc.) of a VM. It has to work out the
    vmid based on the VM name that is passed.
    '''
    #print("starting")

    ## Add some logic so that is vm_name is actually an integer assume its the vm_id however if string its a name

    # Check if the VM is managed bu UCSD or ICF
    # Need to work out some logic that if it exisst on both ICF and UCSD (as could be powered on on prem post migration).
    print("Working out the vmid")
    vmid = VMNameToID(env, vm_name)
    print("The vmid is" + str(vmid))
    if env == "ucsd":
        #print("UCSD env selected")
    # If UCSD follow the following
    # check the power status and work out if needs to actually execute
        apioperation = "userAPIExecuteVMAction"
        generic_actions = ["discardSaveState",
                           "pause",
                           "powerOff",
                           "powerOn",
                           "reboot",
                           "rebuildServer",
                           "repairVM",
                           "reset",
                           "resume",
                           "saveState",
                           "shutdownGuest",
                           "standby",
                           "suspend"]
        if action == "help": return generic_actions
        if not any(action == a for a in generic_actions): return "Action not valid"

        #r = ucsdCall(apioperation, vmid, action, comment)

    elif env == "icfb":
    # If ICF do this instead
        generic_actions = ["powerOff",
                           "powerOn",
                           "reboot",
                           "terminate"]
        if action == "help": return generic_actions
        if not any(action == a for a in generic_actions): return "Action not valid"

        if action == "powerOff":
            apioperation = "Intercloud:userAPIVmPowerOff"
        elif action == "powerOn":
            apioperation = "Intercloud:userAPIVmPowerOn"
        elif action == "reboot":
            apioperation = "Intercloud:userAPIVmReboot"
        elif action == "terminate":
            apioperation = "Intercloud:userAPIVmTerminate"

    else:
        r = "Error, VM not found"

    print "About to " + action + " the VM '" + vm_name + "' with VM_ID '" +str(vmid)+ "' ."
    #env = "icfb"
    r = apiCall(env, apioperation, str(vmid), action, comment)

    return r

## ICF Additions

# def createIPPool(policyName, staticIpPool, vlanId, gatewayIp, subnetMask):
#     '''
#     Creates the static IP address pool and returns the policy identifier.
#     :param0 policyName: Policy name for use with the static IP address pool
#     :param1 staticIpPool: IP Address pool range
#     :param2 vlanId: VLAN identifier.
#     :param3 gatewayIp: Gateway IP address.
#     :param4 subnetMask: Subnet mask for the IP address pool.
#     :return: None
#     '''
#     env = "ucsd"
#     apioperation = "Intercloud:userAPIcreateStaticIPPool"
#
#     # validate IP address
#
#     #is subnetMask a prefic ie /24 or full mask 255.255.255.0
#
#     r = apiCall(env, apioperation)

#################### Catalog Operations ########################################
# Catalog operation APIs enable users to self-provision virtual machines (VMs)
# using predefined catalog items. A catalog item is #created by the system
# administrator and defines the parameters, such as the cloud name and group
# name, to which the VM is bound.
################################################################################

def GetCatalogs(env, group):
    '''
    Returns the catalogs for the specified user group or all groups.
    :param: GroupName
    :return: APITabularReport
    '''

    if group == "all":
        apioperation = "userAPIGetAllCatalogs"
        r = apiCall(env, apioperation)
    else:
        apioperation = "userAPIGetCatalogsPerGroup"
        r = apiCall(env, apioperation, group)

    return r


def GetIconURL(imageId):
    '''
    Returns the icon image URL of the specified icon identifier. Only ICF API!
    :param: imageId
    :return: FormLOVPair[]
    '''

    env = "icfb"
    apioperation = "userAPIGetIconImageURL"

    r = apiCall(env, apioperation, imageId)
    return r

#################### Cloud Operations ##########################################
# The following APIs enable you to perform cloud-related operations. Only ICF.
################################################################################

def GetvCenter(env, vCenterAccountName):
    '''
    Returns a list of all VMware vCenter servers or of all data centers that match the VMware vCenter account name.
    :param: None or vCenterAccountName
    :return: APITabularReport
    '''
    if env == "":
        env = "icfb"
    elif env == "icfb":
        env = env
    else:
        error = "Not a valid environment, only 'icfb' is an option"
        return error

    if vCenterAccountName == "all" or vCenterAccountName == "":
        apioperation = "Intercloud:userAPIGetAllVCenters"
        r = apiCall(env, apioperation)
    else:
        apioperation = "Intercloud:userAPIGetAllDataCenters"
        r = apiCall(env, apioperation, vCenterAccountName)

    return r

def GetClouds(env):
    '''
    Returns a list of all Cisco Intercloud Fabric clouds.
    :param: None
    :return: APITabularReport
    '''
    if env == "":
        env = "icfb"
    elif env == "icfb":
        env = env
    else:
        error = "Not a valid environment, only 'icfb' is an option"
        return error

    apioperation = "Intercloud:userAPIGetAllicfClouds"

    r = apiCall(env, apioperation)
    return r

def GetTunnelProfiles(env):
    '''
    Returns a list of all tunnel profiles.
    :param: None
    :return: APITabularReport
    '''
    if env == "":
        env = "icfb"
    elif env == "icfb":
        env = env
    else:
        error = "Not a valid environment, only 'icfb' is an option"
        return error

    apioperation = "Intercloud:userAPIGetAllTunnelProfiles"

    r = apiCall(env, apioperation)
    return r

def GetCloudSummary(env, icfCloudId):
    '''
    Returns the details of the Cisco Intercloud Fabric clouds that match the specified cloud identifier.
    :param icfCloudId: Cisco Intercloud Fabric cloud identifier.
    :return: APITabularReport
    '''
    if env == "":
        env = "icfb"
    elif env == "icfb":
        env = env
    else:
        error = "Not a valid environment, only 'icfb' is an option"
        return error

    apioperation = "Intercloud:userAPIGeticfCloudSummary"

    r = apiCall(env, apioperation, icfCloudId)
    return r

def GetVMvNics(env, vmId):
    '''
    Returns a list of the vNICs configured on the specified VM.
    :param vmId: VM identifier available from the VM report screen.
    :return: APITabularReport
    '''
    if env == "":
        env = "icfb"
    elif env == "icfb":
        env = env
    else:
        error = "Not a valid environment, only 'icfb' is an option"
        return error

    apioperation = "Intercloud:userAPIGetVMVnics"

    r = apiCall(env, apioperation, vmId)
    return r

#################### Network Operations ########################################
# The following APIs enable you to perform network-related operations. Only ICF.
################################################################################


def GetMgmtPortProfiles(env, vmManager, dataCenter):
    # Not been able to test yet as dont know the param values to pass
    '''
    Returns a list of all management port profiles for the specified VM Manager and data center.
    :param vmManager: VM Manager identifier.
    :param dataCenter: Data center identifier.
    :return: APITabularReport
    '''
    apioperation = "Intercloud:userAPIGetAllPvtMgmtPortProfiles"

    r = apiCall(env, apioperation, vmManager, dataCenter)
    return r

def GetStaticIPPoolPolicies(env):
    '''
    Returns a list of all static IP address pool policies.
    :param None
    :return: APITabularReport
    '''
    apioperation = "Intercloud:userAPIGetAllStaticIPPoolPolicy"

    r = apiCall(env, apioperation)
    return r

def GetStaticIPPool(env):
    ## looks like wants param0, the doc indicates no parm is required however
    # doesnt work as expected. I have raised the qu to the doc author.
    '''
    Returns a list of all static IP address pools.
    :param id
    :return: APITabularReport
    '''

    apioperation = "Intercloud:userAPIGetAllStaticIPPools"

    r = apiCall(env, apioperation, "2")
    return r

def GetResIP(env):
    '''
    Returns a list of all reserved IP addresses.
    :param None
    :return: APITabularReport
    '''

    apioperation = "Intercloud:userAPIGetIPAddressPool"

    r = apiCall(env, apioperation)
    return r

#################### VDC Operations ############################################
# Virtual data center (VDC) management APIs define VDCs based on physical,
# virtual, or public cloud resources. A VDC is an environment that combines
# virtual resources, operational details, rules, and policies to manage specific
# group requirements.
################################################################################


def GetAllVDCs(env):
    # Not been able to test yet as dont know the param values to pass
    '''
    Returns all VDCs for the logged-in user group
    :param None
    :return: APITabularReport
    '''
    apioperation = "userAPIGetAllVDCs"

    r = apiCall(env, apioperation)
    return r

def CreateVDC(env, APIVDCDetails):
    '''
    Creates a vDC defined by the provided data.
    :param: APIVDCDetails
    :return: boolean
    '''
    if env == "":
        env = "ucsd"
    elif env == "ucsd":
        env = env
    else:
        error = "Not a valid environment, only 'ucsd' is an option"
        return error
    apioperation = "userAPICreateVDC"

    # /app/api/rest?formatType=json&opName=userAPICreateVDC&opData={param0:{"vdcName":"sample","vdcDescription":"sample","cloudName":"sample","groupName":1000,"approver1":"sample","approver2":"sample","vdcSupportEmail":"sample","vdcCustomerNoticationEmail":"sample","systemPolicy":"sample","deploymentPolicy":"sample","slaPolicy":"sample","computingPolicy":"sample","storagePolicy":"sample","networkPolicy":"sample","costModel":"sample","isLocked":true,"isDeletable":true,"inactivityPeriodForDeletion":1000,"selfServiceEndUserPolicy":"sample"}}

    values = str(APIVDCDetails)

    print values
    r = apiCall(env, apioperation, values)
    return r

def ExportVDC(env, vdcName):
    '''
    Exports a vDC.
    :param vdcName: Name of the vDC that you want to export
    :return: String
    '''
    if env == "":
        env = "ucsd"
    elif env == "ucsd":
        env = env
    else:
        error = "Not a valid environment, only 'ucsd' is an option"
        return error

    apioperation = "userAPIExportVDC"

    r = apiCall(env, apioperation, vdcName)
    return r

def ImportVDC(env, vdcName):
    # No idea how the hell this one works!!!!
    '''
    Imports a vDC.
    :param vdcName: Name of the vDC that you want to import
    :return: VDC
    '''
    if env == "":
        env = "ucsd"
    elif env == "ucsd":
        env = env
    else:
        error = "Not a valid environment, only 'ucsd' is an option"
        return error

    apioperation = "userAPIImportVDC"

    r = apiCall(env, apioperation, vdcName)
    return r
