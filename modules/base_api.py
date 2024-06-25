import requests
from pydantic import BaseModel, Field
from .token_manager import TokenManager
from .url_helper import model_to_query_string
from modules import GetRecordConfig

class BaseAPI(BaseModel):
    token_manager: TokenManager = Field("", description="Token manager is required to make a request")

    def _build_find_record_endpoint(self, base_token: str, base_table_id: str, record_id: str, config: GetRecordConfig = None):
        if config:
            query_string = model_to_query_string(config)
            return f"https://open.larksuite.com/open-apis/bitable/v1/apps/{base_token}/tables/{base_table_id}/records/{record_id}?{query_string}"

        return f"https://open.larksuite.com/open-apis/bitable/v1/apps/{base_token}/tables/{base_table_id}/records/{record_id}"


    def get_record(self, base_token: str, base_table_id: str, record_id: str, config: GetRecordConfig=None):
        try:
            GET_RECORD_ENDPOINT = self._build_find_record_endpoint(base_token, base_table_id, record_id, config)

            tenant_access_token = self.token_manager.get_tenant_access_token()

            headers = {
                "Authorization": f"Bearer {tenant_access_token}"
            }

            response = requests.get(GET_RECORD_ENDPOINT, headers=headers)


            content = response.json()

            if 'error' in content:
                raise requests.exceptions.RequestException(f"code={content['code']}, msg={content['msg']}, log_id={content['error']['log_id']}")

            return content
        except requests.exceptions.RequestException as err:
            print("Request status:", err)
        

    def list_records(self, base_token: str, base_table_id: str, config: ListRecordQueryParameters=None):

