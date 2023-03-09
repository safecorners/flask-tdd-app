from typing import Optional

from flask import Blueprint
from flask_pydantic import validate
from pydantic import BaseModel

bp = Blueprint("person", __name__)


class QueryParams(BaseModel):
    first_name: Optional[str]
    is_married: Optional[bool]


class CreatePersonRequest(BaseModel):
    first_name: str
    last_name: str
    age: int
    is_married: bool


@bp.route("/person", methods=["GET"])
@validate()
def get(query: QueryParams):
    return query


@bp.route("/person", methods=["POST"])
@validate()
def create(body: CreatePersonRequest):
    return body
