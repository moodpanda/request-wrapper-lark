from modules import TokenManager
from dotenv import load_dotenv
import time
import os

if __name__ == "__main__":

    load_dotenv('.env')
    APP_ID = os.getenv('APP_ID')
    APP_SECRET = os.getenv('APP_SECRET')

    token_manager = TokenManager(
        APP_ID=APP_ID,
        APP_SECRET=APP_SECRET
    )

    uncached_start = time.time()
    token = token_manager.get_app_access_token()
    uncached_end = time.time()
    uncached_duration = uncached_end-uncached_start

    cached_start = time.time()
    token = token_manager.get_app_access_token()
    cached_end = time.time()

    cached_duration = cached_end-cached_start

    print(f"uncache duration: {uncached_duration}")
    print(f"cache duration: {cached_duration}")

    print(f"output: {token}")
    current_time = time.time()
    for i in range(100000):
        cached_start = time.time()
        token = token_manager.get_app_access_token()
        cached_end = time.time()
        print(f"cache duration: {cached_duration}")

    loop_end_time = time.time()
    print(f"loop duration: {loop_end_time-current_time}")