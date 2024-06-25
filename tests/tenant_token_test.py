from modules import TokenManager
import time


token_manager = TokenManager(
    APP_ID="cli_a6889e23ee38500a",
    APP_SECRET="8xCfMdvgQx0G6PEeL6lCkekcg2yFN4yF"
)


start = time.time()

token = token_manager.get_tenant_access_token()

token_uncached_end = time.time()

print(f"uncached: {token_uncached_end-start}")

start = time.time()

token = token_manager.get_tenant_access_token()

token_cached_end = time.time()

print(f"cached: {token_cached_end-start}")