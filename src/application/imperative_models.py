from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import registry

from application.imperative_database import db_session, metadata


class User:
    query = db_session.query_property()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"<User {self.name!r}>"


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), unique=True),
    Column("email", String(120), unique=True),
)

registry().map_imperatively(User, users)
