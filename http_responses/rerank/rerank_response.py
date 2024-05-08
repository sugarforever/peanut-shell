
from pydantic import BaseModel
from models import RerankResult


class RerankResponse(BaseModel):
    results: list[RerankResult]
