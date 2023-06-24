from typing import List, Optional

from pydantic import BaseModel

from .base import ClientInfo


class TrackShipment(BaseModel):
    ClientInfo: ClientInfo
    GetLastTrackingUpdateOnly: Optional[bool] = True
    Shipments: List[int]
