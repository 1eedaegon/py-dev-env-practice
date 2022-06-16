"""Service listers module."""
from .finders import ServiceFinder


class ServiceLister:
    def __init__(self, service_finder: ServiceFinder):
        self._service_finder = service_finder

    def service_version_by(self, version):
        return [service for service in self._service_finder.find_all() if service.version == version]

    def service_released_in(self, timestamp):
        return [service for service in self._service_finder.find_all() if service.timestamp == timestamp]
