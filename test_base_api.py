import os
from modules import BaseAPI, TokenManager, GetRecordConfig
from dotenv import load_dotenv

load_dotenv()

def test_base_api_get_record():
    APP_ID = os.getenv('APP_ID')
    APP_SECRET = os.getenv('APP_SECRET')

    token_manager = TokenManager(APP_ID=APP_ID, APP_SECRET=APP_SECRET)

    base_api = BaseAPI(token_manager=token_manager)

    fetched_record = base_api.get_record(
        base_token="LYLzbg2z0aNuUzsLaX8uLZE3spj",
        base_table_id="tblPDHZfXgZ4Qsjk",
        record_id="recugFDMbfT8oH"
    )

    print(fetched_record)

def test_base_api_get_record_config():
    APP_ID = os.getenv('APP_ID')
    APP_SECRET = os.getenv('APP_SECRET')

    token_manager = TokenManager(APP_ID=APP_ID, APP_SECRET=APP_SECRET)

    base_api = BaseAPI(token_manager=token_manager)

    config = GetRecordConfig()

    fetched_record = base_api.get_record(
        base_token="LYLzbg2z0aNuUzsLaX8uLZE3spj",
        base_table_id="tblPDHZfXgZ4Qsjk",
        record_id="recugFOOpGZAwJ",
        config=config
    )

    print(fetched_record)


# test_base_api_get_record()
test_base_api_get_record_config()

