.. DecorMPI documentation master file, created by
   sphinx-quickstart on Mon Dec 31 16:49:38 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DecorMPI
========

The DecorMPI is a package designed to make running Python functions in an
MPI environment created by using ``mpirun`` or ``mpiexec``.  By simply
decorating your function, like so:

.. code-block:: python

   @decormpi.mpirun(nprocs=4)
   def my_function(*args, **kwargs):
       ...

DecorMPI will convert your function into a stand-alone executable and run
this executable (via a forked subprocess) with ``mpirun``.  It's as easy
as that!  Just decorate, and your functions will be run with ``mpirun``!

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   howitworks
   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
