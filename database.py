import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Author: Ioannis Tsaloumas
# We use create_engine to create an SQLAlchemy engine. This is the connection to the database.
# We using sessionmaker function to create a session that allow us to interact with the database.
# We use beclarative_base() in order to manage the models we define as tables in the database.

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
     Exception("The DATABASE_URL are not defined. Please define the enviroment variable.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, autoflush=False, bind=engine)
Base = declarative_base()