from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel


class PartyAddress(BaseModel):
    CountryCode: str
    City: str
    StateOrProvinceCode: Optional[str]
    PostCode: Optional[str]
    BuildingNumber: Optional[str]
    BuildingName: Optional[str]
    Floor: Optional[str]
    Apartment: Optional[str]
    POBox: Optional[str]
    Description: Optional[str]
    Line1: Optional[str] = ""
    Line2: Optional[str] = ""
    Line3: Optional[str] = ""
    Longitude: Optional[float] = 0
    Latitude: Optional[float] = 0


class Contact(BaseModel):
    PersonName: str
    PhoneNumber1: str
    CellPhone: str
    PhoneNumber1Ext: str = ""
    PhoneNumber2: str = ""
    Department: str = ""
    Title: str = ""
    CompanyName: str = ""
    EmailAddress: str = ""
    Type: str = ""


class Shipper(BaseModel):
    AccountNumber: str
    Reference1: int
    Reference1332: int
    PartyAddress: PartyAddress
    Contact: Contact


class Consignee(BaseModel):
    AccountNumber: str
    PartyAddress: PartyAddress
    Contact: Contact


class ActualWeight(BaseModel):
    Unit: str
    Value: int


class Details(BaseModel):
    Dimensions: Optional[str]
    ActualWeight: ActualWeight
    ChargeableWeight: Optional[str]
    DescriptionOfGoods: str
    GoodsOriginCountry: str
    NumberOfPieces: int
    ProductGroup: str
    ProductType: str
    PaymentType: str
    Services: Optional[str]
    PaymentOptions: Optional[str]
    CashOnDeliveryAmount: Optional[str]
    CustomsValueAmount: Optional[str]
    InsuranceAmount: Optional[str]
    CashAdditionalAmount: Optional[str]
    CollectAmount: Optional[str]
    Items: List[str]


class Shipment(BaseModel):
    Shipper: Shipper
    Consignee: Consignee
    ShippingDateTime: datetime
    Comments: str
    Details: Details
    ForeignHAWB: str
    TransportType: int
    Number: Optional[str]


# NOTE: Aramex doesn't support any type of authentication like JWT or OAuth
# so we have to send these credentials with every request
class ClientInfo(BaseModel):
    UserName: str
    Password: str
    Version: str
    AccountNumber: str
    AccountPin: str
    AccountEntity: str
    AccountCountryCode: str
    Source: int


class CreateShipmentPayload(BaseModel):
    ClientInfo: ClientInfo
    Shipments: List[Shipment]

