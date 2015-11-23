from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='cecs',
      version='0.1',
      description='Cisco Enterprise Cloud Suite',
      long_description='Cisco Enterprsie Cloud Suite',
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
      ],
      include_package_data=True,
      zip_safe=False)
