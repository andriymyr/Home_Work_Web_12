import configparser
import pathlib
import os

from dotenv import load_dotenv

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from starlette import status


load_dotenv()

username = os.environ.get("user")
password = os.environ.get("password")
db_name = os.environ.get("db_name")
domain = os.environ.get("domain")

url = f"postgresql://{username}:{password}@{domain}:5432/{db_name}"
Base = declarative_base()
engine = create_engine(url, echo=False, pool_size=5)

DBSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)

print(f"{'*'*50} \n", url)


# Dependency
def get_db():
    print(f"{'-'*50} \n")
    db = DBSession()
    print(f"{'+'*50} \n", db)
    try:
        yield db
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    finally:
        db.close()


db_1 = get_db()
print(db_1)
