import csv
from repository.base import Repository
from ..models import User, Photo

class CSVRepository(Repository):
    def __init__(self, model, filename="data.csv", pk_field="object_id"):
        self.filename = filename
        self.model = model
        self.pk_field = pk_field
    
    # Create a CSV file if it doesn't exist
    # This method will create a new CSV file if it doesn't exist and write the header row.
    # If the file already exists, it will append to it.
    def create(self, obj):
        with open(self.filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=obj.dict().keys())
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(obj.dict())
        return obj
    

    # Reads CSV file by id and returns the object
    # This method reads the CSV file and returns the object with the specified id.
    # If the object is not found, it returns None.
    def read(self, object_id):
        with open(self.filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row[self.pk_field]) == object_id:
                    return self.model(**row)
        return None

    # Returns a list of all objects in the CSV file
    # This method reads the CSV file and returns a list of all objects.

    def list_all(self, obj):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return [self.model(**row) for row in csv.DictReader(f)]

    def update(self, obj_id, obj):
            rows = []
            updated = False
            with open(self.filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if int(row[self.pk_field]) == object_id:
                        rows.append(obj.dict())
                        updated = True
                    else:
                        rows.append(row)
            if updated:
                with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=obj.dict().keys())
                    writer.writeheader()
                    writer.writerows(rows)
            return obj if updated else None

    def delete(self, object_id):
        rows = []
        deleted = False
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row[self.pk_field]) != object_id:
                    rows.append(row)
                else:
                    deleted = True
        if deleted:
            with open(self.filename, 'w', newline='') as f:
                fieldnames = rows[0].keys() if rows else self.model.__fields__.keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)