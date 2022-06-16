"""Main module."""
from dependency_injector.wiring import Provide, inject

from .containers import Container
from .listers import ServiceLister


@inject
def main(lister: ServiceLister = Provide[Container.lister]) -> None:
    print("Something service:")
    for service in lister.service_version_by("v1.2.2"):
        print("\t-", service)

    print("Created at 20220614")
    for service in lister.service_released_in(20220622):
        print("\t-", service)


if __name__ == "__main__":
    container = Container()
    container.config.finder.type.from_env("SERVICE_FINDER_TYPE")
    container.wire(modules=[__name__])

    main()
