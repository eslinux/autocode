import asyncio

async def say_hello(a : int) -> int:
    await asyncio.sleep(1)
    print('Hello, World!')
    return a




ret = asyncio.run(say_hello(a=123))

print(ret)

# Output:
# (After a one-second pause) 'Hello, World!'
