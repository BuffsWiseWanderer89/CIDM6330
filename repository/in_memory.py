from repository.base import Repository

class InMemoryRepository(Repository):
    def __init__(self):
        self.storage = []
    
    def create(self, obj):
        self.storage.append(obj)
        return obj
    
    def read(self, object_id):
        return next((item for item in self.storage if item.object_id == object_id), None)

    def update(self, object_id, obj):
        for index, item in enumerate(self.storage):
            if item.object_id == object_id:
                self.storage[index] = obj
                return obj
        return None
    
    def delete(self, object_id):
        self.storage = [item for item in self.storage if item.id != object_id]
    
    def list_all(self):
        return self.storage