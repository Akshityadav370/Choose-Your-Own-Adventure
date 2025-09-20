from sqlalchemy import create_engine
# create_engine wraps around the DB we are interacting (just like bridge)
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from core.config import settings

engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# we need these for our models, as it inherits all the sql properties, so we can use sql orm on our models

def get_db():
    # gets a DB session
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)