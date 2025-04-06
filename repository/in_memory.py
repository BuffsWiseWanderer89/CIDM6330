from repository.base import Repository

class InMemoryRepository(Repository):
    def __init__(self):
        self.storage = []
    
    def create(self, obj):
        self.storage.append(obj)
        return obj
    
    def read(self, id):
        return next((item for item in self.storage if item.id == id), None)

    def update(self, id, obj):
        for i in item in enumerate(self.storage):
            if i.id == id:
                self.storage[i] = obj
                return obj
        return None
    
    def delete(self, id):
        self.storage = [item for item in self.storage if item.id != id]
    
    def list_all(self):
        return self.storage
    
