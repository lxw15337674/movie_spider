import threading
import asyncio

async def hello():
    print('1')
    await asyncio.sleep(1)
    print('2')
    await asyncio.sleep(1)
    print('3')

async def bye():
    print('9')
    print('8')

loop = asyncio.get_event_loop()
tasks = [hello(), hello(),bye()]
loop.run_until_complete(asyncio.wait(tasks))
loop.run_until_complete()
loop.close()