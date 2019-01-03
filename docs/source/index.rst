.. mpirical documentation master file, created by
   sphinx-quickstart on Mon Dec 31 16:49:38 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mpirical
========

The ``mpirical`` package is designed to make it easy to execute
Python code in its own, dedicated MPI environment.  It works by
providing a decorator called ``mpirical.mpirun`` which acts like
a MPI's ``mpirun`` utility.  Every time you execute an
``mpirical``-decorated function, that function will run in its
own MPI environment, with the number of processes specified,
as if it had been made into an MPI executable and run with
``mpirun`` from the command-line.

For example, consider some ``mpi4py`` code in a file called
``my_mpi_script.py``:

.. code-block:: python

   def function():
       from mpi4py import MPI
       comm = MPI.COMM_WORLD
       rank = comm.Get_rank()

       if rank == 0:
           print('Hello, everyone!')
       else:
           print('And hello to you, rank 0!')

   if __name__ == '__main__':
       function()

You would normally need to execute this with MPI's ``mpirun``,
like so:

.. code-block:: bash

   mpirun -np 4 python my_mpi_script.py

With ``mpirical``, you can accomplish the same thing by simply
decorating the ``function`` function and then executing it, like so:

.. code-block:: python

   import mpirical

   @mpirical.mpirun(np=4)
   def function():
       from mpi4py import MPI
       comm = MPI.COMM_WORLD
       rank = comm.Get_rank()

       if rank == 0:
           print('Hello, everyone!')
       else:
           print('And hello to you, rank 0!')

   function()

When this script is executed, the ``function`` code will be executed
with 4 MPI processes, just as if it were run with ``mpirun``
previously.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   motivation
   howitworks
   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
