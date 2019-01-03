Motivation
----------

The ``mpirical`` package was originally written to make it easy to
run MPI-parallel Python unit tests (i.e., tests of MPI parallel Python
code that require a fixed number of processes in order to execute
correctly).  With ``mpi4py``, this has always been possible, but to
make this work, one had to run your tests with an explicit use of
``mpirun``, like so:

.. code-block:: bash

   mpirun -np 8 pytest -v my_package/tests/

While this method of running parallel MPI tests works, Imaging the
scenario where you have a mix of tests that require different numbers
of MPI ranks.  For example, suppose some tests are serial, some are
parallel and require more than 2 ranks, and some are parallel and
require *exactly* 2 ranks.  In order to run all of these tests, one
would need to run your tests in blocks with different ``mpirun``
calls, like so:

.. code-block:: bash

   pytest -v my_package/serial_tests/
   mpirun -np 2 pytest -v my_package/rank2_tests/
   mpirun -np 4 pytest -v my_package/rank4_tests/

and so on.  Wouldn't it be so much better to simply run:

.. code-block:: bash

   pytest -v mypackage/tests/

and have each test indicate how many processes they need themselves?

That's the motivation behind ``mpirical``, and while testing was the
primary motivation, it is not the only thing for which ``mpirical``
can be used.  I encourage you to come up with other clever uses for
``mpirical``, but if you just use it for testing, that's fine, too.
