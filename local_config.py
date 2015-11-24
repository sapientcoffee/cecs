'''
    Site specific configuration details for an implementation.
    Used to store server info, authentication keys, base urls, etc

    Update with your relevant information before running CLI scripts OR using the xxxd_library.py modules
'''

# UCS Director Access Info  -  Update for your install
ucsdserver = ""
ucsd_key = ""

# Secondary UCS Director Access Info
ucsdserver_sec = ""
ucsd_key_sec = ""

# ICF Director Access Info  -  Update for your Install
icfbserver = ""
icfb_key = ""

# This information should stay the same for all users
url = "https://%s/app/api/rest?"
getstring = "formatType=json&opName=%s"
parameter_lead = "&opData="
headers = {"X-Cloupia-Request-Key":" "}
