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
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='https://github.com/clijockey/CECS',
      author='clijockey',
      author_email='rob.j.edwards@gmail.com',
      license='MIT',
      packages=['cecs'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/cecs-cli'],
      entry_points={
          'console_scripts': ['cecs-joke=cecs.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
