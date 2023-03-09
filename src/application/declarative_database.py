from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(
#     "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
# )
engine = create_engine("sqlite:///:memory:")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db() -> None:
    import application.declarative_models

    Base.metadata.create_all(bind=engine)

    u = application.declarative_models.User("hello", "hello@example.com")
    db_session.add(u)
    db_session.commit()
