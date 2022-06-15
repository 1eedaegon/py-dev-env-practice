"""Service finders module."""

import csv
from typing import Callable, List

from .entities import Service


# 서비스 Factory: 직접 구현 방지 및 상속 구현 강제
class ServiceFinder:
    def __init__(self, service_factory: Callable[..., Service]) -> None:
        self._service_factory = service_factory

    def find_all(self) -> List[Service]:
        raise NotImplementedError()


class CsvServiceFinder(ServiceFinder):
    def __init__(self, service_factory: Callable[..., Service], path: str, delimeter: str) -> None:
        self._csv_file_path = path
        self._delimiter = delimiter
        super().__init__(service_factory)

    def find_all(self) -> List[Service]:
        with open(self._csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self._delimiter)
            return [self._service_factory(*row) for row in csv_reader]
