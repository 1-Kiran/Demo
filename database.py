from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url="postgresql://postgres:admin@localhost:5432/akira"
engine=create_engine(db_url)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)