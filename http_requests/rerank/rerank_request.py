from pydantic import BaseModel

CROSS_ENCODER_MODELS = [
    "ms-marco-TinyBERT-L-2-v2",
    "ms-marco-MiniLM-L-2-v2",
    "ms-marco-MiniLM-L-4-v2",
    "ms-marco-MiniLM-L-6-v2",
    "ms-marco-MiniLM-L-12-v2",
    "ms-marco-TinyBERT-L-2",
    "ms-marco-TinyBERT-L-4",
    "ms-marco-TinyBERT-L-6",
    "ms-marco-electra-base"
]

class RerankRequest(BaseModel):
    model: str
    query: str
    top_n: int
    documents: list[str]
