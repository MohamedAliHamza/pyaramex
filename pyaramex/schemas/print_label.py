from pydantic import BaseModel

from .base import ClientInfo


class LabelInfo(BaseModel):
    ReportID: int
    ReportType: str


class PrintLabel(BaseModel):
    ClientInfo: ClientInfo
    LabelInfo: LabelInfo
    ShipmentNumber: int
