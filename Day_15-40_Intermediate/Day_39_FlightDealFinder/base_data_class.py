import logging
from pprint import pprint
from abc import ABC, abstractmethod

import requests

logging.basicConfig(level=logging.INFO, format="%(levelname)s: [%(funcName)s] %(message)s")
logger = logging.getLogger(__name__)


class BaseDataClass(ABC):


    @property
    @abstractmethod
    def get_url(self):
        """Наследник обязан определить базовый URL."""
        raise NotImplementedError

    @staticmethod
    def classify_response(status_code: int, name: str = "") -> None:
        match status_code:
            case 200 | 201 | 204:
                logger.info("Success code: %d", status_code, stacklevel=2)
            case 301 | 302:
                logger.warning("Redirect code:%d", status_code, stacklevel=2)
            case status_code if 400 <= status_code < 500:
                logger.error("Client error status code:%d", status_code, stacklevel=2)
            case status_code if status_code >= 500:
                logger.error("Server error status code:%d", status_code, stacklevel=2)
            case _:
                logger.error("Unknown status code:%d", status_code, stacklevel=2)


    @staticmethod
    def _get(endpoint: str, payload: dict, headers: dict) -> requests.Response:
        response = requests.get(url=endpoint, json=payload, headers=headers, timeout=5)
        # pprint(response.json())
        response.raise_for_status()
        return response

    @staticmethod
    def _post(endpoint: str, payload: dict, headers: dict) -> requests.Response:
        response = requests.post(url=endpoint, json=payload, headers=headers, timeout=5)
        pprint(response.json())
        response.raise_for_status()
        return response
