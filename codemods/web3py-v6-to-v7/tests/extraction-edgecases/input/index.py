from web3 import Web3

# 1. Nested factory function with heavy indentation
class MiddlewareFactory:
    def get_logger(self):
        def deep_nested_logger(make_request, w3):
            # This comment has trailing spaces    
            
            def middleware(method, params):
                """
                Docstring inside
                """
                print("logging")
                return make_request(method, params)
            return middleware
        return deep_nested_logger

# 2. Decorators and type hints
@my_custom_decorator(arg=True)
@another_decorator
def typed_middleware(make_request: Callable, w3: "Web3") -> Callable:
    def middleware(method, params):
        pass
    return middleware

# 3. Trailing comments attached to the node
def comment_middleware(make_request, w3):
    pass
