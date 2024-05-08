from sentence_transformers import CrossEncoder
from models import RerankResult
from http_requests import RerankRequest
from http_responses import RerankResponse
from services.rerank_service import RerankService


class CrossEncoderRerankService(RerankService):

    def __init__(self, modelName: str) -> None:
        super().__init__()
        self.cross_encoder = CrossEncoder(model_name=modelName)

    def rerank(self, request: RerankRequest) -> RerankResponse:
        pairs = []
        for document in request.documents:
            pairs.append([request.query, document])

        scores = self.cross_encoder.predict(pairs)

        scored_pairs = list(zip(scores, range(len(request.documents))))
        scored_pairs.sort(key=lambda x: x[0], reverse=True)

        # Generate a list of indices in descending order of their corresponding scores
        results = [RerankResult(index=index, relevance_score=score) for score, index in scored_pairs]

        return RerankResponse(results=results[:request.top_n])