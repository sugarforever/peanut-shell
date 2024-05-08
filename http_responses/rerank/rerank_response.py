
from pydantic import BaseModel
from models import RerankResult


class RerankModelsResponse(BaseModel):
    models: list[str]


class RerankResponse(BaseModel):
    results: list[RerankResult]
