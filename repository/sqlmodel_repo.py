from sqlmodel import Session, select
from repository.base import Repository

class SQLModelRepository(Repository):
    def __init__(self, model, session: Session):
        self.model = model
        self.session = session

    def create(self, obj):
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def read(self, object_id):
        return self.session.get(self.model, object_id)

    def update(self, object_id, obj):
        db_obj = self.session.get(self.model, object_id)
        if db_obj:
            for key, value in obj.dict(exclude_unset=True).items():
                setattr(db_obj, key, value)
            self.session.commit()
            self.session.refresh(db_obj)
            return db_obj
        return None

    def delete(self, object_id):
        obj = self.session.get(self.model, object_id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False

    def list_all(self):
        return self.session.exec(select(self.model)).all()
