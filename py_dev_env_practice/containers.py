"""Containers module."""

from dependency_injector import containers, providers

from . import entities


class Container(containers.DeclarativeContainer):
    movie = providers.Provider(entities.Movie)  # type: ignore
