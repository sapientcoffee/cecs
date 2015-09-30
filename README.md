# CECS

This is my first attempt at creating a Python Module and is intended to assist with using the Cisco Enterprise Cloud Suite APIs. The initial work will be around UCS Director.

This have been inspired and influenced by https://github.com/hpreston/cisco_cloud. I initially intended to contribute to Hanks good work however as a learning exercise I wanted to create my own module and learn how to use unit testing for it.

Once you have pulled the module down you should browse into the directory and execute;

    python setup.py install


To use (with caution), simply do::

    >>> import cecs
    >>> print cecs.getsr()

I will at some stage (once it is in a useful state) publish on PyPI to allow much easier installation.


### Working Functions
The modules is most defiantly work in progress, the following functions are working;

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |



### Example Scripts
