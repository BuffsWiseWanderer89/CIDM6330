from abc import ABC, abstractmethod


# creates class that inherits from ABS and implements the abstract methods
# this is a base class for all repositories
class Repository(ABC):
    @abstractmethod
    def create(self, obj): ...
    
    @abstractmethod
    def read(self, id, obj): ...
    
    @abstractmethod
    def update(self, id, obj): ...

    @abstractmethod
    def delete(self, id): ...

    @abstractmethod
    def list_all(self): ...