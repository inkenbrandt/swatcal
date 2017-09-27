from __future__ import absolute_import, division, print_function, unicode_literals
from setuptools import setup
import os
import sys

if not sys.version_info[0] in [2, 3]:
    print('Sorry, wellapplication not supported in your Python version')
    print('  Supported versions: 2 and 3')
    print('  Your version of Python: {}'.format(sys.version_info[0]))
    sys.exit(1)  # return non-zero value for failure

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except:
    pass

setup(name='swatcal',
      version='0.3.0',
      description='Libraries for performing nsga2 calibration.',
      long_description='Calibration tools for SWAT models',
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT License",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Development Status :: Alpha"
          "Intended Audience :: Science/Research",
          "Natural Language :: English",
      ],
      url='https://github.com/inkenbrandt/swatcal',
      author='Mehmet B. Ercan',
      author_email='ercanm@email.sc.edu',
      license='MIT',
      packages=['swatcal'],
      install_requires=['numpy', 'spotpy'],
      data_files=[(os.path.join('swatcal', 'ScriptsForSWATtxt'),
                   [os.path.join('swatcal', 'ScriptsForSWATtxt', 'Extract_rch.py'),
                    os.path.join('swatcal', 'ScriptsForSWATtxt', 'SWAT_ParameterEdit.py'),
                    os.path.join('swatcal', 'ScriptsForSWATtxt', 'Makefile'),
                    os.path.join('swatcal', 'ScriptsForSWATtxt', 'swat2012_627'),
                    os.path.join('swatcal', 'ScriptsForSWATtxt', 'nsga2_mid.sh'),
                    os.path.join('swatcal', 'ScriptsForSWATtxt', 'nsga2_mid.cmd'),
                    os.path.join('swatcal', 'ScriptsForSWATtxt', 'swat.exe'), ])],
      include_package_data=True
      )
