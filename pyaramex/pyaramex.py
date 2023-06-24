import requests
from requests.models import Response
from pydantic import ValidationError

from .settings import URLSettings, Environment
from .schemas import(
    PrintLabel,
)


class Aramex:

    def __init__(self, env: Environment) -> None:
        if env == Environment.Dev:
            self.config = URLSettings(_env_file="pyaramex/.envs/.dev")
        elif env == Environment.Prod:
            self.config = URLSettings(_env_file="pyaramex/.envs/.prod")
        else:
            raise ValueError("env must be either dev or prod")

    def create_shipment(self, payload) -> Response:
        raise NotImplementedError

    def track_shipment(self, payload) -> Response:
        raise NotImplementedError

    def print_label(self, payload: dict) -> Response:
        try:
            payload = PrintLabel(**payload)
        except ValidationError as e:
            return e.errors()

        response = requests.post(
            url=self.config.PrintLabel,
            data=payload.dict(),
        )
        return response
