from web3.providers.websocket import (
    WebSocketProvider
)
from web3.datastructures import CustomAttributeDict

async def main():
    provider = WebSocketProvider(endpoint_uri="ws://...")
    w3 = WebSocketProvider(
        "ws://..."
    )
    timeout = w3.socket.timeout
    w3.socket.process()
    
    try:
        pass
    except (ABIEventNotFound, ABIFunctionNotFound) as e:
        pass
    except ABIEventNotFound:
        pass
