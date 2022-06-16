"""Service finders module."""

import csv
import sqlite3
from typing import Callable, List

from .entities import Service


# 서비스 Factory: 직접 구현 방지 및 상속 구현 강제
class ServiceFinder:
    def __init__(self, service_factory: Callable[..., Service]) -> None:
        self._service_factory = service_factory

    def find_all(self) -> List[Service]:
        raise NotImplementedError()


class CsvServiceFinder(ServiceFinder):
    def __init__(self, service_factory: Callable[..., Service], path: str, delimiter: str) -> None:
        self._csv_file_path = path
        self._delimiter = delimiter
        super().__init__(service_factory)

    def find_all(self) -> List[Service]:
        with open(self._csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self._delimiter)
            return [self._service_factory(*row) for row in csv_reader]


class SqliteServiceFinder(ServiceFinder):
    def __init__(self, service_factory: Callable[..., Service], path: str) -> None:
        self._database = sqlite3.connect(path)
        super().__init__(service_factory)

    def find_all(self) -> List[Service]:  # type: ignore
        with self._database as db:
            rows = db.execute("SELECT name, timestamp, version FROM services")
            return [self._service_factory(*row) for row in rows]
