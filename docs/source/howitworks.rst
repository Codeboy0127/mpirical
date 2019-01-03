How It Works
============

The magic behind the ``mpirical`` package is serialization!

When an ``mpirical``-decorated function is executed, the ``mpirical.mpirun``
decorator executes the function code with the following procedure:

- the decorated function and its arguments are serialized,

- the serialized function-arguments are written to a file,

- a subprocess is created in which an ``mpirun`` command is executed, running
  an ``mpi4py``-enabled script that (in parallel)

  - reads the serialized function-arguments file,
  - deserializes the function and its arguments,
  - executes the function with the given arguments in a ``try``-block,
  - performs an MPI ``gather`` on the results from each MPI process,
  - serializes the gathered results,
  - writes the results to a file,

- reads the serialized results file,

- deserializes the results, and

- returns the deserialized results.

Thanks to the magic of ``dill``, ``cloudpickle``, and Python's internal
``pickle``, this procedure works with most Python code, and thanks to
the ``tblib`` package, any errors that are encountered can be captured,
serialized, and re-raised on the main process with accurate tracebacks!
