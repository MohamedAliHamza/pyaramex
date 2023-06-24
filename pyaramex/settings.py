from enum import Enum

from pydantic import BaseSettings, AnyUrl


class URLSettings(BaseSettings):
    CreateShipment: AnyUrl
    TrackShipment: AnyUrl
    PrintLabel: AnyUrl


class Environment(str, Enum):
    Dev = "dev"
    Prod = "prod"
