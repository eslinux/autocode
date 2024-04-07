# https://medium.com/@shilosadon/python-multiple-tasks-886513ae2cd4

import asyncio


async def func_a():
    print("Function A is running")
    await asyncio.sleep(3)
    print("Function A is done")
    return "Function A"


async def func_b():
    print("Function B is running")
    await asyncio.sleep(1)
    print("Function B is done")
    return "Function B"


async def main():
    print("Main function is running")
    # This is where both tasks are started concurrently.
    # asyncio.gather() is used to run async functions in parallel,
    # not waiting for one to complete before starting the next.
    results = await asyncio.gather(func_a(), func_b())
    print("Main function is done")
    print(results)


asyncio.run(main())


# Main function is running
# Function A is running
# Function B is running
# Function B is done
# Function A is done
# Main function is done
# ['Function A', 'Function B']