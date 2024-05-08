from pydantic import BaseModel


class RerankResult(BaseModel):
    index: int
    relevance_score: float
