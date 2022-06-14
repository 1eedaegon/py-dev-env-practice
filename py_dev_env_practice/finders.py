"""Service finders module."""

import csv
from typing import Callable, List

from .entities import ServiceEntity


# 서비스 Factory: 직접 구현 방지 및 상속 구현 강제
class ServiceFinder:
    def __init__(self, service_factory: Callable[..., ServiceEntity]) -> None:
        self._service_factory = service_factory

    def find_all(self) -> List[ServiceEntity]:
        raise NotImplementedError()


class CsvServiceFinder(ServiceFinder):
    def __init__(self, service_factory: Callable[..., ServiceEntity], path: str, delimeter: str) -> None:
        self._csv_file_path = path
        self._delimeter = delimeter
        super().__init__(service_factory)

    def find_all(self) -> List[ServiceEntity]:
        with open(self._csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self._delimeter)
            return [self._service_factory(*row) for row in csv_reader]
