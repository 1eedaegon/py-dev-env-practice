"""Service entities module."""


class ServiceEntity:
    def __init__(self, name: str, timestamp: int, version: str):
        self.name = str(name)
        self.timestamp = int(timestamp)
        self.version = str(version)

    def __repr__(self):
        return "{0}(name={1}, timestamp={2}, version={3}".format(
            self.__class__.__name__,
            repr(self.name),
            repr(self.timestamp),
            repr(self.version),
        )
