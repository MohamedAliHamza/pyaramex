from .schemas import CreateShipmentPayload


class Aramex:
    def __init__(self, env: str) -> None:
        pass

    def create_shipment(self, payload: CreateShipmentPayload) -> dict:
        raise NotImplementedError

    def track_shipment(self, awb):
        raise NotImplementedError
    
    def print_label(self, awb):
        raise NotImplementedError
