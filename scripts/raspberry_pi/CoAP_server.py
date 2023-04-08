#!/usr/bin/env python3

"""This retrieves fingerprint data, encrypts it via public key, 
and then sends the encrypted data on request"""

import os
import datetime
import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from time import sleep

# load the fingerprint data
        
class HelloWorldResource(resource.Resource):

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




