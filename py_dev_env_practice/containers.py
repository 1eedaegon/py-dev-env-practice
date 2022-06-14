"""Containers module."""

from dependency_injector import containers


class Container(containers.DeclarativeContainer):
    def hello(self):
        return
