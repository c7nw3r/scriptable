from abc import ABC, abstractmethod
from typing import Optional, Union

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