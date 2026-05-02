from typing import Callable
from web3 import Web3

# 1. Multiple functions in the same file to test dynamic CI mock naming
class FirstMiddleware(Web3Middleware):
    def request_processor(self, method, params):
        print(f"Request: {method}")
        return method, params

class SecondMiddleware(Web3Middleware):
    def request_processor(self, method, params):
        print(f"Request: {method}")
        return method, params

# 2. Middleware name containing underscores that need camelCasing
class MyVeryCustomLoggerMiddleware(Web3Middleware):
    def request_processor(self, method, params):
        print(f"Request: {method}")
        return method, params
