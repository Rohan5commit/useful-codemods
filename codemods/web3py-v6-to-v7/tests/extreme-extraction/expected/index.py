from typing import Callable
from web3 import Web3

# Extreme Case 1: Multiline parameters with type hints and default values
class HeavyMiddleware(Web3Middleware):
    def request_processor(self, method, params):
        print(f"Request: {method}")
        return method, params

# Extreme Case 2: Function that has make_request and w3 in its BODY, but NOT in parameters
def innocent_function(api_key: str):
    make_request = "not a real request"
    w3 = "not a real w3"
    print(make_request, w3)

# Extreme Case 3: Middleware defined completely on one line (Minified Python)
class MinifiedMiddleware(Web3Middleware):
    def request_processor(self, method, params):
        print(f"Request: {method}")
        return method, params
