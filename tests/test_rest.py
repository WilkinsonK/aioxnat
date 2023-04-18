import pytest

from aioxnat.protocols import AsyncRestAPI
from aioxnat.objects import Experiment, FileData, Scan


class TestRESTClient:

    def test_get_experiments(self, experiment):
        assert isinstance(experiment, Experiment),\
            "Expected instance of 'Experiment'."

    def test_get_scans_from_project(self, scan_by_project):
        assert isinstance(scan_by_project, Scan),\
            "Expected instance of 'Scan'."

    def test_get_scans_from_experiment(self, scan_by_experiment):
        assert isinstance(scan_by_experiment, Scan),\
            "Expected instance of 'Scan'."

    def test_get_resources(self, resources):
        assert isinstance(resources[0], FileData),\
            "Expected instance of 'FileData'."
