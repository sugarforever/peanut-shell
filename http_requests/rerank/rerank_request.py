from pydantic import BaseModel


class RerankRequest(BaseModel):
    query: str
    top_n: int
    documents: list[str]
