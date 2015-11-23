"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cecs',
      version='0.1.dev2',
      description='Cisco Enterprise Cloud Suite',
      long_description=long_description,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='cecs ucsd icfb cisco',
      url='https://github.com/clijockey/CECS',
      author='clijockey',
      author_email='rob.j.edwards@gmail.com',
      license='MIT',
      packages=['cecs'],
      install_requires=[
          'markdown',
          'requests',
          'json',
          'colorama',
      ],
      include_package_data=True,
      zip_safe=False)
