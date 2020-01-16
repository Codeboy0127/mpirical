from os.path import exists
from setuptools import setup, find_packages

if exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = ''

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: MacOS',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering',
]

setup(
    name='mpirical',
    description='Decorate any function to make it run in parallel with MPI',
    long_description=long_description,
    python_requires='>=3.6',
    maintainer='Kevin Paul',
    maintainer_email='kpaul@ucar.edu',
    classifiers=CLASSIFIERS,
    url='https://github.com/NCAR/mpirical',
    packages=find_packages(exclude=('mpirical.tests',)),
    package_dir={'mpirical': 'mpirical'},
    include_package_data=True,
    install_requires=install_requires,
    license='Apache 2.0',
    zip_safe=False,
    keywords=['mpirical', 'MPI', 'mpi4py'],
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
)
