import asyncio

async def do_something_long_time(a : int) -> int:
    print("start")
    await asyncio.sleep(3)
    print("finished")
    return a

async def main():
    retDosomething = await do_something_long_time(a=123)
    return retDosomething

ret = asyncio.run(main())
print(ret)
