from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

MYSQL_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(MYSQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
