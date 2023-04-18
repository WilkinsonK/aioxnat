import asyncio, os, time

import pytest, dotenv

from aioxnat.objects import validator
from aioxnat.rest import SimpleAsyncRestAPI

dotenv.load_dotenv()

event_loop = asyncio.get_event_loop_policy().get_event_loop()
"""
Running event loop used in fixtures that require
asyncio.
"""


def dummy_function(*args, **kwds):
    time.sleep(0.01)
    return (args, kwds)


@pytest.fixture
def generic_callable():
    return dummy_function


@pytest.fixture
def validator_callable():
    return validator(dummy_function)


@pytest.fixture
def xnat_project():
    return os.getenv("XNAT_REST_PROJECT", None)


@pytest.fixture(autouse=True)
def rest_api():
    return SimpleAsyncRestAPI\
        (
            os.getenv("XNAT_HOSTNAME", ""),
            username=os.getenv("XNAT_REST_USERNAME", None),
            password=os.getenv("XNAT_REST_PASSWORD", None)
        )


@pytest.fixture
def experiment(rest_api, xnat_project):

    async def inner():
        async with rest_api:
            it = rest_api.get_experiments(xnat_project)
            return (await anext(it))[0]

    return event_loop.run_until_complete(inner())


@pytest.fixture
def scan_by_project(rest_api, xnat_project):

    async def inner():
        async with rest_api:
            it = rest_api.get_scans(xnat_project)
            return (await anext(it))[0]

    return event_loop.run_until_complete(inner())


@pytest.fixture
def scan_by_experiment(rest_api, experiment):

    async def inner():
        async with rest_api:
            it = rest_api.get_scans(experiment)
            return (await anext(it))[0]

    return event_loop.run_until_complete(inner())


@pytest.fixture
def resources(rest_api, scan_by_project):

    async def inner():
        async with rest_api:
            return await rest_api.resources(scan_by_project, "DICOM")

    return event_loop.run_until_complete(inner())
