from abc import ABC, abstractmethod
from typing import Optional, Union, Callable

PropertySource = Union[dict, 'PropertyResolver']


class PropertyResolver(ABC):

    @abstractmethod
    def __getitem__(self, item) -> Optional[str]:
        pass

    @abstractmethod
    def __setitem__(self, key: str, value):
        pass

    @abstractmethod
    def __contains__(self, item):
        pass


class DictPropertyResolver(PropertyResolver):
    def __init__(self, properties: dict):
        self.properties = properties

    def __getitem__(self, item) -> Optional[str]:
        return self.properties[item]

    def __setitem__(self, key: str, value):
        self.properties[key] = value

    def __contains__(self, item):
        return item in self.properties


class LambdaPropertyResolver(DictPropertyResolver):
    def __init__(self, properties: dict, callback: Callable[[str], Optional[str]]):
        super().__init__(properties)
        self.callback = callback

    def __getitem__(self, item) -> Optional[str]:
        result = super().__getitem__(item)
        return result if result is not None else self.callback(item)

    def __contains__(self, item):
        return self.__getitem__(item) is not None
