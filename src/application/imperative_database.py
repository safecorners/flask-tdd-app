from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(
#     "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
# )
engine = create_engine("sqlite:///:memory:")
metadata = MetaData()
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


def init_db() -> None:
    metadata.create_all(bind=engine)
