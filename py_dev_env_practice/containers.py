"""Containers module."""

from dependency_injector import containers, providers

from . import entities, finders, listers


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(yaml_files=["config.yml"])

    service = providers.Factory(entities.Service)  # type: ignore

    csv_finder = providers.Singleton(
        finders.CsvServiceFinder, service_factory=service.provider, path=config.finder.csv.path, delimiter=config.finder.csv.delimiter
    )

    lister = providers.Factory(listers.ServiceLister, service_finder=csv_finder)
