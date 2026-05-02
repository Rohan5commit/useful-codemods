from typing import Callable
from web3 import Web3

# Extreme Case 1: Multiline parameters with type hints and default values
def heavy_middleware(
    make_request: Callable[[str, list], dict] = None,
    w3: "Web3" = None,
    logger_name: str = "default"
) -> Callable:
    """
    Docstring here.
    """
    def middleware(method, params):
        # We also have an internal variable named make_request just to mess with greedy matchers
        local_make_request = make_request
        return local_make_request(method, params)
    return middleware

# Extreme Case 2: Function that has make_request and w3 in its BODY, but NOT in parameters
def innocent_function(api_key: str):
    make_request = "not a real request"
    w3 = "not a real w3"
    print(make_request, w3)

# Extreme Case 3: Middleware defined completely on one line (Minified Python)
def minified_middleware(make_request, w3): return lambda method, params: make_request(method, params)
