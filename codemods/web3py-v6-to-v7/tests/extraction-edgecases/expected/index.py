from web3 import Web3

# 1. Nested factory function with heavy indentation
class MiddlewareFactory:
    def get_logger(self):
        class DeepNestedLogger(Web3Middleware):
            def request_processor(self, method, params):
                print(f"Request: {method}")
                return method, params
        return deep_nested_logger

# 2. Decorators and type hints
@my_custom_decorator(arg=True)
@another_decorator
class TypedMiddleware(Web3Middleware):
    def request_processor(self, method, params):
        print(f"Request: {method}")
        return method, params

# 3. Trailing comments attached to the node
class CommentMiddleware(Web3Middleware):
    def request_processor(self, method, params):
        print(f"Request: {method}")
        return method, params
