#!/usr/bin/env python
from setuptools import setup
import versioneer

setup(name='mpi-pytest',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='A pytest-friendly package to run parallel MPI tests',
      author='Kevin Paul',
      author_email='kpaul@ucar.edu',
      url='https://github.com/NCAR/mpi-pytest',
      license='https://www.apache.org/licenses/LICENSE-2.0',
      packages=['mpi_pytest'],
      package_dir={'mpi_pytest': 'mpi_pytest'},
      package_data={'mpi_pytest': ['LICENSE']},
      install_requires=['mpi4py']
      )
