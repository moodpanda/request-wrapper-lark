from modules import TokenManager

APP_ID="cli_a6889e23ee38500a"
APP_SECRET="8xCfMdvgQx0G6PEeL6lCkekcg2yFN4yF"

def test_get_tenant_access_token():
    token_manager = TokenManager(APP_ID=APP_ID, APP_SECRET=APP_SECRET)

    token = token_manager.get_tenant_access_token()
    print(token)


