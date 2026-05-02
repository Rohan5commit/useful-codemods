from web3.providers.websocket import (
    WebsocketProviderV2
)
from web3.datastructures import AttributeDict, CustomAttributeDict

async def main():
    provider = WebsocketProviderV2(endpoint_uri="ws://...")
    w3 = AsyncWeb3.persistent_websocket(
        "ws://..."
    )
    timeout = w3.ws.timeout
    w3.ws.process()
    
    try:
        pass
    except (ABIEventFunctionNotFound, ABIFunctionNotFound) as e:
        pass
    except ABIEventFunctionNotFound:
        pass
