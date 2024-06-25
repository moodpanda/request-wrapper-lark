from pydantic import BaseModel
from typing import Literal

class ParentAccessTokenPayload(BaseModel):
    app_id: str
    app_secret: str

class ParentAccessTokenResponse(BaseModel):
    code: int
    msg: str
    expire: int

class TenantAccessTokenResponse(ParentAccessTokenResponse):
    tenant_access_token: str
    
class AppAccessTokenResponse(ParentAccessTokenResponse):
    app_access_token: str

class GetRecordConfig(BaseModel):
    text_field_as_array: bool = False
    user_id_type: Literal["user_id", "union_id", "open_id"] = "open_id"
    display_formula_ref: bool = False
    with_shared_url: bool = False
    automatic_fields: bool = True

