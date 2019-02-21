import pytest


def pytest_addoption(parser):
    parser.addoption("--mpiunstable", action="store_true",
                     help="run only OpenMPI unstable tests")
    parser.addoption("--nompiunstable", action="store_true",
                     help="skip all OpenMPI unstable tests")


def pytest_runtest_setup(item):
    test_is_mpiunstable = 'mpiunstable' in item.keywords
    only_run_mpiunstable = item.config.getvalue("mpiunstable")
    never_run_mpiunstable = item.config.getvalue("nompiunstable")
    if only_run_mpiunstable:
        if not test_is_mpiunstable:
            pytest.skip("only running OpenMPI unstable tests")
    elif never_run_mpiunstable:
        if test_is_mpiunstable:
            pytest.skip("skipping OpenMPI unstable tests")
