from typing import Optional

from flask import Blueprint
from flask_pydantic import validate
from pydantic import BaseModel

bp = Blueprint("batch", __name__)


class AddBatchRequest(BaseModel):
    ref: str
    sku: str
    qty: int
    eta: Optional[str]


@bp.route("/batch", methods=["POST"])
@validate()
def create(body: AddBatchRequest):
    return body
