from pkg_resources import DistributionNotFound, get_distribution

from mpirical.decorator import mpirun  # noqa: F401

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
