from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
# SQLACHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/' 
# '<database_name'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Sessionlocal()
    try: 
        yield db
    finally:
        db.close()

# database: fastapi_ab2x
# password: 8ACdJkK5CQQM8zDf1PHojPi0j89HnXQp
# internal database url: postgresql://fastapiuser:8ACdJkK5CQQM8zDf1PHojPi0j89HnXQp@dpg-d69087o6fj8s73cavho0-a/fastapi_ab2x
#external database url:  postgresql://fastapiuser:8ACdJkK5CQQM8zDf1PHojPi0j89HnXQp@dpg-d69087o6fj8s73cavho0-a.oregon-postgres.render.com/fastapi_ab2x
# postqresql command: PGPASSWORD=8ACdJkK5CQQM8zDf1PHojPi0j89HnXQp psql -h dpg-d69087o6fj8s73cavho0-a.oregon-postgres.render.com -U fastapiuser fastapi_ab2x
# while True:

#   try:
#       conn = psycopg2.connect(host = 'localhost', database= 'fastapi', user= 'postgres', password='root', cursor_factory=RealDictCursor)
#       cursor = conn.cursor()
#       print("Database connection as successful!")
#       break
#   except Exception as error:
#       print("Connecting to database failed")
#       print("Error: ", error)
#       time.sleep(2)