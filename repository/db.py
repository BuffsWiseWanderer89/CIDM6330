from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, class_=Session, expire_on_commit=False)

def get_session():
    with SessionLocal() as session:
        yield session
    