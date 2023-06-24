from typing import Optional

from pydantic import BaseModel


# NOTE: Aramex doesn't support any type of authentication like JWT or OAuth
# so we have to send these credentials with every request
class ClientInfo(BaseModel):
    UserName: str
    Password: str
    Version: Optional[str] = "v1"
    AccountNumber: str
    AccountPin: str
    AccountEntity: str
    AccountCountryCode: str
    Source: Optional[int] = 24
