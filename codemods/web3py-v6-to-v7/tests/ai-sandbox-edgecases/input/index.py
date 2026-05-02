from typing import Callable
from web3 import Web3

# 1. Multiple functions in the same file to test dynamic CI mock naming
def first_middleware(make_request: Callable, w3: "Web3") -> Callable:
    def middleware(method, params):
        pass
    return middleware

def second_middleware(make_request: Callable, w3: "Web3") -> Callable:
    def middleware(method, params):
        pass
    return middleware

# 2. Middleware name containing underscores that need camelCasing
def my_very_custom_logger_middleware(make_request, w3):
    def middleware(method, params):
        pass
    return middleware
