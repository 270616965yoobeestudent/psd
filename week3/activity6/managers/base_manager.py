from abc import ABC, abstractmethod


class BaseManager(ABC):
    @abstractmethod
    def get(self, **args):
        pass

    @abstractmethod
    def list(self, **args):
        pass

    @abstractmethod
    def add(self, **args):
        pass

    @abstractmethod
    def delete(self, **args):
        pass

    @abstractmethod
    def update(self, **args):
        pass
