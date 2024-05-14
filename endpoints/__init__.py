from fastapi import APIRouter, HTTPException
from http_requests import RerankRequest, CROSS_ENCODER_MODELS
from http_responses import RerankModelsResponse, RerankResponse
from services import CrossEncoderRerankService

router = APIRouter()


@router.get("/models/", response_model=RerankModelsResponse)
def models():
    return RerankModelsResponse(models=CROSS_ENCODER_MODELS)


@router.post("/rerank/", response_model=RerankResponse)
def rerank(request: RerankRequest):
    if request.model not in CROSS_ENCODER_MODELS:
        detail = f"Invalid model name: {request.model}. Available models: {','.join(CROSS_ENCODER_MODELS)}"
        raise HTTPException(status_code=400, detail=detail)

    if len(request.documents) == 0:
        raise HTTPException(status_code=400, detail="invalid request: list of documents must not be empty")

    model_name = f"cross-encoder/{request.model}"
    service = CrossEncoderRerankService(modelName=model_name)
    return service.rerank(request)
