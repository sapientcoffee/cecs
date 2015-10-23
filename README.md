# CECS

This is my first attempt at creating a Python Module and is intended to assist with using the Cisco Enterprise Cloud Suite APIs. The initial work will be around UCS Director.

This have been inspired and influenced by https://github.com/hpreston/cisco_cloud. I initially intended to contribute to Hanks good work however as a learning exercise I wanted to create my own module and learn how to use unit testing for it.

Once you have pulled the module down you should browse into the directory and execute;

    python setup.py install


To use (with caution), simply do::

    >>> import cecs
    >>> print cecs.getsr()

I will at some stage (once it is in a useful state) publish on PyPI to allow much easier installation.

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
Examples that have been created using the module are the following.

#### ui.py
This script provides a text base menu to do display various things. The menu should be self explanatory.
