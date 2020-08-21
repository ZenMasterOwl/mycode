#!/usr/bin/env python3

import asyncio
from datetime import datetime as dt
import time

async def swiss():
    await asyncio.sleep(1)
    print(f"Swiss: {dt.now()}")

async def loopadoop():
    for each in range(10):
        print("kaboom" + str(each))

async def main():
    # Most preferred way to write async code
    task3 = asyncio.create_task(swiss())
    task4 = asyncio.create_task(swiss())
    task5 = asyncio.create_task(loopadoop())
    await asyncio.gather(task3, task4,task5)
    await asyncio.gather(for each in range(2):
            asyncio.create_task(loopadoop()))

if __name__ == "__main__":
    asyncio.run(main())
