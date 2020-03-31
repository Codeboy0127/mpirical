========
mpirical
========

|Circle| |Docs| |Codecov|

The ``mpirical`` package provides an easy way to execute parallel Python code (or any Python function)
in parallel with MPI.  It uses the ``mpi4py`` package to enable parallel MPI executation in Python, but
unlike ``mpi4py`` on its own, ``mpirical`` automatically executes decorated functions with ``mpirun``
or ``mpiexec`` *for you*, instead of requiring that the user run their Python code with ``mpirun`` or
``mpiexec`` explicitly.  All of this is done in the background!

See the documentation_ for more details.


LICENSE
-------

Apache 2.0 (See `License File <https://www.apache.org/licenses/LICENSE-2.0>`__)

.. _documentation: https://mpirical.readthedocs.io
    
.. |Circle| image:: https://img.shields.io/circleci/build/gh/NCAR/mpirical?style=for-the-badge
    :target: https://circleci.com/gh/NCAR/mpirical/tree/master

.. |Docs| image:: https://readthedocs.org/projects/mpirical/badge/?version=latest&style=for-the-badge
    :target: https://mpirical.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |Codecov| image:: https://img.shields.io/codecov/c/gh/NCAR/mpirical?style=for-the-badge
    :target: https://codecov.io/gh/NCAR/mpirical
