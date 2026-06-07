from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base


class DB(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")


db_class = DB()
engine = create_engine(db_class.database_url, pool_pre_ping=True)


@event.listens_for(engine, "connect")
def set_client_encoding(dbapi_connection, connection_record):
    dbapi_connection.set_client_encoding("UTF8")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
