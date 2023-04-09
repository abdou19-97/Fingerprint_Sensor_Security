#!/usr/bin/env python3

"""This is a usage example of aiocoap that demonstrates how to implement a
simple server. See the "Usage Examples" section in the aiocoap documentation
for some more information."""

import os
import datetime
import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from time import sleep
        
class HelloWorldResource(resource.Resource):
    """Example resource which supports the GET method. It uses asyncio.sleep to
    simulate a long-running operation, and thus forces the protocol to send
    empty ACK first. """

    def get_link_description(self):
        # Publish additional data in .well-known/core
        return dict(**super().get_link_description(), title="Hello World Request")

    async def render_get(self, request):
        await asyncio.sleep(3)

        payload = "<<<Hello World!>>>".encode('ascii')
        return aiocoap.Message(payload=payload)
    
# logging setup
logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

async def main():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(['.well-known', 'core'],
            resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(['helloWorld'], HelloWorldResource())

    await aiocoap.Context.create_server_context(root, bind=("149.162.135.83", 5683))

    # Run forever
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())


