from modules import KVStore 
import time


def test_store_kv_insert():
    cache = KVStore()

    cache.put("hello", "world")

    assert cache.get("hello") == "world"

def test_store_kv_delete():
    cache = KVStore()
    cache.put("hello", "world")
    cache.trash("hello")

    assert cache.get("hello") == None

def test_store_kv_expiration():
    cache = KVStore()

    cache.put("hello", "world", expiration=1)

    time.sleep(2)

    assert cache.get("hello") == None

def test_store_kv_store_not_expired():
    cache = KVStore()

    cache.put("hello", "world", expiration=3)

    assert cache.get("hello") == "world"
