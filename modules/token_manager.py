from pydantic import BaseModel, Field
from .models import ParentAccessTokenPayload, TenantAccessTokenResponse, AppAccessTokenResponse
from .kv_store import KVStore
import os
import requests
import logging

class TokenManager(BaseModel):
    TENANT_ACCESS_TOKEN_ENDPOINT: str = "https://open.larksuite.com/open-apis/auth/v3/tenant_access_token/internal"
    APP_ACCESS_TOKEN_ENDPOINT: str = "https://open.larksuite.com/open-apis/auth/v3/app_access_token/internal"
    USER_ACCESS_TOKEN_ENDPOINT: str = "https://open.larksuite.com/open-apis/authen/v1/oidc/access_token"
    APP_ID: str = Field("", description="The bot application id is required")
    APP_SECRET: str = Field("", description="The bot application secret is required")
    cache: KVStore = KVStore()

    def get_tenant_access_token(self):
        cached = self.cache.get("tenant_token")
        if cached:
            return cached
        try:
            payload = ParentAccessTokenPayload(app_id=self.APP_ID, app_secret=self.APP_SECRET)
            response = requests.post(self.TENANT_ACCESS_TOKEN_ENDPOINT, data=payload.model_dump_json())
            token_response = TenantAccessTokenResponse.model_validate(response.json())

            tenant_access_token = token_response.tenant_access_token

            # cache the tenant access token
            self.cache.put(
                key="tenant_token",
                value=tenant_access_token,
                expiration=token_response.expire
            )

            return tenant_access_token 
        except requests.exceptions.RequestException as err:
            logging.error(f"fetching tenant_access_token failure: {err}")
            response.raise_for_status()
    
    def get_app_access_token(self):
        cached = self.cache.get("app_token")

        if cached:
            return cached
        
        try:
            payload = ParentAccessTokenPayload(app_id=self.APP_ID, app_secret=self.APP_SECRET)

            response = requests.post(self.APP_ACCESS_TOKEN_ENDPOINT, data=payload.model_dump_json())

            token_response = AppAccessTokenResponse.model_validate(response.json())

            app_access_token = token_response.app_access_token

            self.cache.put(
                key="app_token",
                value=app_access_token,
                expiration=token_response.expire
            )

            return app_access_token
        
        except requests.exceptions.RequestException as err:
            logging.error(f"fetching app_access_token failure: {err}")
            response.raise_for_status()

