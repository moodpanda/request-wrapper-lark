import time
from pydantic import BaseModel
from typing import Dict, Any, Union

class KVStore(BaseModel):
    store: Dict[str, Dict[str, Any]] = {}
    expirations: Dict[str, float] = {}

    def get(self, key: str) -> Any | None:
        if key in self.store:
            if key in self.expirations:
                expiration = self.expirations[key]

                current_time = int(time.time())
                if current_time > expiration:
                    return None
                else:
                    return self.store[key]
            else:
                return self.store[key]
        else:
            return None

    
    def put(self, key: str, value: Any, expiration: Union[float, None] = None) -> None:
        if not expiration:
            self.store[key] = value
        else:
            self.expirations[key] = time.time() + expiration
            self.store[key] = value
    
    def trash(self, key: str) -> None:
        del self.store[key]
    
    def length(self) -> int:
        return len(self.store)
        