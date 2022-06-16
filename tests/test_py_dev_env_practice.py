"""Test module."""

from unittest import mock

import pytest
from py_dev_env_practice.containers import Container


@pytest.fixture
def container():
    container = Container(
        config={
            "finder": {
                "type": "csv",
                "csv": {
                    "path": "/fake-services.csv",
                    "delimiter": ",",
                },
                "sqlite": {
                    "path": "/fake-services.db",
                },
            }
        }
    )
    return container


def test_services_version_by(container):
    finder_mock = mock.Mock()
    finder_mock.find_all.return_value = [
        container.service("Backend service", 20220616, "v1.1.1"),
        container.service("Frontend service", 20220616, "v2.1.2"),
    ]
    with container.finder.override(finder_mock):
        lister = container.lister()
        services = lister.service_version_by("v2.1.2")

    assert len(services) == 1
    assert services[0].name == "Frontend service"


def test_services_released_in(container):
    finder_mock = mock.Mock()
    finder_mock.find_all.return_value = [
        container.service("Proxy service", 20220617, "v1.1.1"),
        container.service("Load balancer service", 20220617, "v2.1.2"),
    ]
    with container.finder.override(finder_mock):
        lister = container.lister()
        services = lister.service_released_in(20220617)

    assert len(services) != 2
    assert services[0].name == "Load balancer service"
