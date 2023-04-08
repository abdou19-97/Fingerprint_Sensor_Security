#!/usr/bin/env python3

"""This uses CoAP to retrieve encrypted fingerprint data 
from the raspberry pi and then decrypts the data 
using a private key"""

import logging
import asyncio

from aiocoap import *
from aiocoap.numbers import GET

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://149.162.135.83/helloWorld')

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.run(main())
