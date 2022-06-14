"""Containers module."""

from dependency_injector import containers, providers

from . import entities, finders


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(yaml_files=["config.yml"])

    service = providers.Provider(entities.Service)  # type: ignore

    csv_finder = providers.Singleton(
        finders.CsvServiceFinder, service_factory=service.provider, path=config.finder.csv.path, delimiter=config.finder.csv.delimete
    )
