from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

#nameOfDatabase+driver://<username>:<password>@<server>/<database>?driver=<driver_name>
#loading environment variable from .env
load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")

#sqlAlchemy engine
engine=create_engine(DATABASE_URL)

#session factoryyy
SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()