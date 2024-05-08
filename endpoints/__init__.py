from fastapi import APIRouter
from http_requests import RerankRequest
from http_responses import RerankResponse
from services import CrossEncoderRerankService

router = APIRouter()

@router.post("/rerank/", response_model=RerankResponse)
def rerank(request: RerankRequest):
    service = CrossEncoderRerankService("cross-encoder/ms-marco-MiniLM-L-6-v2")
    return service.rerank(request)