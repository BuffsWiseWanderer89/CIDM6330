from abc import ABC, abstractmethod


# creates class that inherits from ABS and implements the abstract methods
# this is a base class for all repositories
class Repository(ABC):
    @abstractmethod
    def create(self, obj): ...
    
    @abstractmethod
    def read(self, object_id): ...
    
    @abstractmethod
    def update(self, object_id, obj): ...

    @abstractmethod
    def delete(self, object_id): ...

    @abstractmethod
    def list_all(self): ...