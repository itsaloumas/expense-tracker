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
    raise EnvironmentError(
        "Environment variable DATABASE_URL is not set. "
        "Example: export DATABASE_URL='mariadb+mariadbconnector://user:pass@localhost:3306/expense_db'"
    )

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()