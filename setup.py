#!/usr/bin/env python3

from distutils.core import setup

setup(name='JCMBSoft Python Library',
      version='2.00',
      description='JCMBsoft Python Library',
      author='JCMBsoft',
      author_email='Geoffrey@jcmbsoft.com',
      url='https://jcmbsoft.com/',
      license="For JCMBsoft code, MIT For Trimble, GPL V3 for everyone else. Other code per orginal source",
      packages=['JCMBSoftPyLib'],
      package_dir={'JCMBSoftPyLib': '.'}
     )
