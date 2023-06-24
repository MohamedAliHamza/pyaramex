import requests
from requests.models import Response

from .settings import URLSettings, Environment
from .utils import validate_payload
from .schemas import(
    PrintLabel,
    TrackShipment,
)


class Aramex:

    def __init__(self, env: Environment) -> None:
        if env == Environment.Dev:
            self.config = URLSettings(_env_file="pyaramex/.envs/.dev")
        elif env == Environment.Prod:
            self.config = URLSettings(_env_file="pyaramex/.envs/.prod")
        else:
            raise ValueError("env must be either dev or prod")

    def create_shipment(self, payload: dict) -> Response:
        raise NotImplementedError

    @validate_payload
    def track_shipment(self, payload: dict) -> Response:
        payload = TrackShipment(**payload)
        response = requests.post(
            url=self.config.TrackShipment,
            data=payload.dict(),
        )
        return response

    @validate_payload
    def print_label(self, payload: dict) -> Response:
        payload = PrintLabel(**payload)        
        response = requests.post(
            url=self.config.PrintLabel,
            data=payload.dict(),
        )
        return response
