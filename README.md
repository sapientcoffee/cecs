# CECS

This is my first attempt at creating a Python Module and is intended to assist with using the Cisco Enterprise Cloud Suite APIs. The initial work will be around UCS Director.

This has been inspired and influenced by https://github.com/hpreston/cisco_cloud. I initially intended to contribute to Hanks good work however as a learning exercise I wanted to create my own module and learn how to package and use unit testing for it.

This is still a work in progress project and is evolving when I get time to work on it, if you would like to assist with the development please reach out to me or make pull requests etc.

Once you have pulled the module down you should browse into the directory and execute;

    python setup.py install

Once that has completed you will need to configure your UCSD/ICFB hostnames and API key to allow your scripts to communicate with the servers. The CECS module will look for the file ```~/.cecs.cfg``` which will contained the required.

```
[UCSD]
apikey = 4522D0E068144D66666B15F2F1D8FD2A
hostname = ucsd.domain.com
[ICFB]
apikey = 6B75494C86E0416666AA390A98033922
hostname = ucsd.domain.com
```
You can either create the file and populate yourself or run the script ```obtain_credentials.py``` which is located in the cecs folder. The aim of this script is to make setting up your system much easier, however at the moment the step to pull back you API key automatically isn't working as expected. 

To test, simply obtain the version of UCSD (or ICFB):

    >>> import cecs
    >>> print cecs.version(ucsd)

I will at some stage (once it is in a useful state) publish on PyPI to allow much easier installation (this is half done but has sum bits to work out).

Do you want or need an environment to test against? Well the good news for ICFB is that Cisco DevNet have made a sandbox avaialble. To get more information go to my [blog](http://clijockey.com/intercloud-fabric-api/).


### Working Functions
The module is most defiantly work in progress, the following functions are working (these are only the ones that I think are useful rather than all in the module);

| Fuctions        | Purpose     | Params |
| ------------- |:-------------:|:-------------:|
| getAllVMs      | Gets a list of all VMs for the user | |
| sr_get      | Gets a list of all the service requests       |  |
| GetCatalogs |  Returns the catalogs for the specified user group or all groups. | Environment(UCSD or ICFB) and Group(either group name or all) |
| GetIconURL | Returns the icon image URL of the specified icon identifier. Only ICF API! | imageId |   
| | | |
| GetvCenter | Returns a list of all VMware vCenter servers or of all data centers that match the VMware vCenter account name. | |
| GetClouds | Returns a list of all Cisco Intercloud Fabric clouds. | |
| GetTunnelProfiles | Returns a list of all tunnel profiles. | |
| GetCloudSummary | Returns the details of the Cisco Intercloud Fabric clouds that match the specified cloud identifier. | |
| GetVMvNics | Returns a list of the vNICs configured on the specified VM. | |



### Example Scripts
Examples that have been created using this module are as follows, they reside on the /examples directory;
```
  ├── examples
  │   ├── cecs-cli.py
  │   ├── play.py
  │   └── ui.py
```

#### ui.py
This script provides a text base menu to do display various things. The menu should be self explanatory.


```
~ python ui.py

Welcome, this is an example of using the API for UCS Director and Intercloud Fabric Director

Please choose the menu you want to start:
1. Catalog Items
2. Service Requests
3. Infrastructure

q. Quit
 >>
```

```
 >> 2
Requests Menu!

1. List all UCSD service requests
2. List all ICFB service requests

m. Main Menu
q. Quit
 Requests >>
```

```
Requests >> 1
Obtaining requested data (this may take a minute) .............
Please hold the line caller you are important to us.
All Service Requests!

https://infrastructure.ukidcv.cisco.com/app/api/rest?formatType=json&opName=userAPIGetServiceRequests&opData={}
+-----+---------------------------------------------------------------+------------+---------------------------+-----------+
| ID  |                            Workflow                           | Group/User |            Time           |   Status  |
+-----+---------------------------------------------------------------+------------+---------------------------+-----------+
| 629 |              Linux - CentOS / Provision VMware VM             | Demo/user  | Nov 17, 2015 17:27:38 UTC |  Complete |
| 628 |              Linux - CentOS / Provision VMware VM             | Demo/user  | Nov 17, 2015 17:24:39 UTC |  Complete |
| 627 |              Linux - CentOS / Provision VMware VM             | Demo/user  | Nov 17, 2015 17:19:59 UTC |   Failed  |
| 620 |                 Create Three Tier Application                 |   admin    | Nov 16, 2015 10:41:03 UTC |  Complete |
| 619 |                 Create Three Tier Application                 |   admin    | Nov 16, 2015 10:39:15 UTC |   Failed  |
| 618 |          Rollback Partner Create Tenant Demo (SR 615)         |   admin    | Nov 16, 2015 10:33:26 UTC |  Complete |
| 617 |          Rollback Partner Create Tenant Demo (SR 614)         |   admin    | Nov 16, 2015 10:32:49 UTC |  Complete |
| 616 |     Create ACI Tenant and Network / ACI Tenent and Network    | Demo/user  | Nov 16, 2015 10:31:18 UTC |  Complete |
| 615 |                   Partner Create Tenant Demo                  |   admin    | Nov 16, 2015 10:20:14 UTC |  Complete |
| 614 |                   Partner Create Tenant Demo                  |   admin    | Nov 16, 2015 10:18:02 UTC |  Complete |
| 613 |        Rollback Create Three Tier Application (SR 607)        |   admin    | Nov 16, 2015 09:49:39 UTC |  Complete |
| 607 |                 Create Three Tier Application                 |   admin    | Nov 16, 2015 09:41:47 UTC | Cancelled |
| 606 |              Linux - CentOS / Provision VMware VM             | Demo/admin | Nov 09, 2015 17:49:11 UTC |  Complete |
| 605 |                            AD User                            |   admin    | Nov 02, 2015 12:10:11 UTC |   Failed  |
| 604 |        Rollback Create Three Tier Application (SR 596)        | Demo/admin | Nov 02, 2015 10:51:49 UTC |  Complete |
| 601 |           Select Storage Tier / Provision VMware VM           | Demo/user  | Nov 02, 2015 10:32:22 UTC |  Complete |
| 596 | Deploy Three-tier Application / Create Three Tier Application | Demo/user  | Nov 02, 2015 10:27:25 UTC |  Complete |
| 595 |                       Button - ALter Mem                      | Demo/user  | Nov 02, 2015 10:22:34 UTC |  Complete |
| 580 |         Dummy WF to test Generate_AD_Create_Powershell        |   admin    | Oct 28, 2015 18:34:14 UTC |  Complete |
| 574 |             Rollback Provision VMware VM (SR 571)             |   admin    | Oct 28, 2015 18:16:37 UTC | Cancelled |
| 573 |            Rollback Fenced Container Setup (SR 572)           |   admin    | Oct 28, 2015 18:16:23 UTC |  Complete |
| 572 |                     Fenced Container Setup                    |   admin    | Oct 28, 2015 12:18:31 UTC |  Complete |
| 571 |           Select Storage Tier / Provision VMware VM           | Demo/user  | Oct 28, 2015 12:02:53 UTC |  Complete |
+-----+---------------------------------------------------------------+------------+---------------------------+-----------+

b. Back
q. Quit
 Requests >>
```

#### cecs-cli.py
The idea of this script is to create a command line interface to both UCSD & ICFB. At the moment I havnt got the 'setuptools' working correctly to allow this to run as a true CLI. You can however run the script using ```python cecs-cli.py``` or make the file executable. As a hack I have created an alias to it using cecs (which will be what I use when I work out 'entry_points' on 'setuptools').

You should be able to get help by running ```--help``` on the script. A few example outputs are as follows;

```
~ cecs                                                                                                                                                           
Usage: cecs-cli.py [OPTIONS] COMMAND [ARGS]...

  Cisco Enterprise Cloud Suite Command Line Interface.

  This is a CLI to interact with the compoenents of CECS. Initially this
  only works with UCS Director (UCSD) and Intercloud Fabric for Business
  (ICFB). As this project evolves other tools will be incorporated.

  UCS Director:

  UCSD is a data centre automation and orchestration tool. It manages on-
  premise network, storage and compute (physical & virtual).

  Intercloud Fabric:

  ICFB is hard of the Cisco hybrid cloud strategy that allows, you to extend
  your on-premise networks into provider and public clouds. It also provides
  the capabulities to migrate workloads between clouds taking care of any
  converstion processes.

Options:
  -h, --help  Show this message and exit.

Commands:
  hello    This script works similar to the Unix `cat`...
  list     This will list a number of things managed by...
  order    Order items
  version  Client & server versions
```

Another way to get help.
```
~ cecs --help                                                                                                                                                   
Usage: cecs-cli.py [OPTIONS] COMMAND [ARGS]...

  Cisco Enterprise Cloud Suite Command Line Interface.

  This is a CLI to interact with the compoenents of CECS. Initially this
  only works with UCS Director (UCSD) and Intercloud Fabric for Business
  (ICFB). As this project evolves other tools will be incorporated.

  UCS Director:

  UCSD is a data centre automation and orchestration tool. It manages on-
  premise network, storage and compute (physical & virtual).

  Intercloud Fabric:

  ICFB is hard of the Cisco hybrid cloud strategy that allows, you to extend
  your on-premise networks into provider and public clouds. It also provides
  the capabulities to migrate workloads between clouds taking care of any
  converstion processes.

Options:
  -h, --help  Show this message and exit.

Commands:
  hello    This script works similar to the Unix `cat`...
  list     This will list a number of things managed by...
  order    Order items
  version  Client & server versions
```

Help on a specific option;
```
~ cecs list --help                                                                                                                                              
Usage: cecs-cli.py list [OPTIONS]

  This will list a number of things managed by Cisco Enterprise Cloud Suite.

  Initially this will be UCS Dirctor only and will evolve to use ICFB

Options:
  -i, --item TEXT  Items you want ot list
  -e, --env TEXT   Select the environment, either ucsd or icfb
  -h, --help       Show this message and exit.
```


To pull back all the service requests in UCSD, by default the cli will query ucsd. It can be forces using the ```--env``` flag (```--env ucsd```)
```
~ cecs list                                                                                                                                                     
Listing various things
https://infrastructure.ukidcv.cisco.com/app/api/rest?formatType=json&opName=userAPIGetServiceRequests&opData={}
+-----+---------------------------------------------------------------+------------+---------------------------+-----------+
| ID  |                            Workflow                           | Group/User |            Time           |   Status  |
+-----+---------------------------------------------------------------+------------+---------------------------+-----------+
| 629 |              Linux - CentOS / Provision VMware VM             | Demo/user  | Nov 17, 2015 17:27:38 UTC |  Complete |
| 628 |              Linux - CentOS / Provision VMware VM             | Demo/user  | Nov 17, 2015 17:24:39 UTC |  Complete |
| 627 |              Linux - CentOS / Provision VMware VM             | Demo/user  | Nov 17, 2015 17:19:59 UTC |   Failed  |
| 620 |                 Create Three Tier Application                 |   admin    | Nov 16, 2015 10:41:03 UTC |  Complete |
| 619 |                 Create Three Tier Application                 |   admin    | Nov 16, 2015 10:39:15 UTC |   Failed  |
| 618 |          Rollback Partner Create Tenant Demo (SR 615)         |   admin    | Nov 16, 2015 10:33:26 UTC |  Complete |
| 617 |          Rollback Partner Create Tenant Demo (SR 614)         |   admin    | Nov 16, 2015 10:32:49 UTC |  Complete |
| 616 |     Create ACI Tenant and Network / ACI Tenent and Network    | Demo/user  | Nov 16, 2015 10:31:18 UTC |  Complete |
| 615 |                   Partner Create Tenant Demo                  |   admin    | Nov 16, 2015 10:20:14 UTC |  Complete |
| 614 |                   Partner Create Tenant Demo                  |   admin    | Nov 16, 2015 10:18:02 UTC |  Complete |
| 613 |        Rollback Create Three Tier Application (SR 607)        |   admin    | Nov 16, 2015 09:49:39 UTC |  Complete |
| 607 |                 Create Three Tier Application                 |   admin    | Nov 16, 2015 09:41:47 UTC | Cancelled |
| 606 |              Linux - CentOS / Provision VMware VM             | Demo/admin | Nov 09, 2015 17:49:11 UTC |  Complete |
| 605 |                            AD User                            |   admin    | Nov 02, 2015 12:10:11 UTC |   Failed  |
| 604 |        Rollback Create Three Tier Application (SR 596)        | Demo/admin | Nov 02, 2015 10:51:49 UTC |  Complete |
| 601 |           Select Storage Tier / Provision VMware VM           | Demo/user  | Nov 02, 2015 10:32:22 UTC |  Complete |
| 596 | Deploy Three-tier Application / Create Three Tier Application | Demo/user  | Nov 02, 2015 10:27:25 UTC |  Complete |
| 595 |                       Button - ALter Mem                      | Demo/user  | Nov 02, 2015 10:22:34 UTC |  Complete |
| 580 |         Dummy WF to test Generate_AD_Create_Powershell        |   admin    | Oct 28, 2015 18:34:14 UTC |  Complete |
| 574 |             Rollback Provision VMware VM (SR 571)             |   admin    | Oct 28, 2015 18:16:37 UTC | Cancelled |
| 573 |            Rollback Fenced Container Setup (SR 572)           |   admin    | Oct 28, 2015 18:16:23 UTC |  Complete |
| 572 |                     Fenced Container Setup                    |   admin    | Oct 28, 2015 12:18:31 UTC |  Complete |
| 571 |           Select Storage Tier / Provision VMware VM           | Demo/user  | Oct 28, 2015 12:02:53 UTC |  Complete |
+-----+---------------------------------------------------------------+------------+---------------------------+-----------+
```

To pull back all the service requests from ICFB;
```
~ cecs list --env icfb                                                                                                                                          
Listing various things
https://sandboxicf.cisco.com/app/api/rest?formatType=json&opName=userAPIGetServiceRequests&opData={}
+----+----------+------------+------+--------+
| ID | Workflow | Group/User | Time | Status |
+----+----------+------------+------+--------+
+----+----------+------------+------+--------+
```
#### cecs-cli.py
This is just my scratch pad (test area) until I get unittest setup and run some automated checks. I also use it when working out new things.
