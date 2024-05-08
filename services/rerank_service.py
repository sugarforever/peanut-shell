from abc import ABC, abstractmethod
from http_requests import RerankRequest
from http_responses import RerankResponse


class RerankService(ABC):
    @abstractmethod
    def rerank(self, request: RerankRequest) -> RerankResponse:
        pass
