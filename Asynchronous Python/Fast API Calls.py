import requests
from time import time
from datetime import timedelta
import json
import aiohttp
import asyncio
import threading
import concurrent.futures
from time import time
import requests

URL = "https://api.kanye.rest/"

def get_kanye_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    # print(response.json())
    return response.json()


def get_kanye_quote_map(limit):
    for _ in range(limit):
        response = requests.get(url="https://api.kanye.rest/")
        response.raise_for_status()
        # print(response.json())


# ------------------------------------- Synchronous : Normal http requests Calls ---------------------------------------
def via_request():
    start = time()
    for _ in range(10):
        get_kanye_quote()
        print(get_kanye_quote())

    stop = time()
    duration = stop - start
    print(f"request: {duration} seconds")


# --------------------------------------------- Using requests.Session() -----------------------------------------------
def via_requests_session():
    with requests.Session() as session:
        start = time()
        for _ in range(10):
            get_kanye_quote()

        stop = time()
        duration = stop - start
        print(f"requests.session: {duration} seconds")


# ---------------------------------------- Threading using threading module --------------------------------------------
def via_threading_module():
    from threading import Thread

    threads = []

    start = time()
    for _ in range(10):
        t = Thread(target=get_kanye_quote)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    stop = time()
    duration = stop - start
    print(f"The functions ran via the threading module for {duration} seconds")


# ------------------------------- Threading using the ThreadPoolExecutor and submit()-----------------------------------
def via_threadpoolexecutor_submit():
    from concurrent.futures import ThreadPoolExecutor

    start = time()
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(10):
            f = executor.submit(get_kanye_quote)
            futures.append(f)

        for future in concurrent.futures.as_completed(futures):
            future.result()
            print(future.result())

    duration = time() - start
    print(f"The functions ran via ThreadPoolExecutor class and submit method for {duration} seconds")


# ------------------------------- Threading using the ThreadPoolExecutor and map()--------------------------------------
def via_threadpoolexecutor_map():
    from concurrent.futures import ThreadPoolExecutor

    start = time()
    futures = []
    limit = [10]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(get_kanye_quote_map, limit)

    duration = time() - start
    print(f"The functions ran via ThreadPoolExecutor class and map method for {duration} seconds")


# ---------------------------------------------- aiohttp + asyncio.run() -----------------------------------------------
def via_aiohttp():
    import asyncio
    import aiohttp

    start_time = time()

    async def get_kanye_async():
        async with aiohttp.ClientSession() as session:
            for _ in range(10):
                result = await session.get(url="https://api.kanye.rest/")
                print(await result.json())

    asyncio.run(get_kanye_async())
    duration = time() - start_time
    print(f"aiohttp: {duration} seconds")


# ------------------------------------------------- aiohttp + tasks ----------------------------------------------------
def via_aiohttp_tasks():
    results = []
    start_time = time()

    def get_tasks(session, url):
        tasks = []
        for _ in range(10):
            task = session.get(url)
            # task = asyncio.create_task(session.get(url))
            tasks.append(task)
        return tasks

    async def get_kanye_quote_coro():
        async with aiohttp.ClientSession() as session:
            tasks = get_tasks(session, URL)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                print(await response.json())
                result = await response.json
                results.append(result)

        return results

    asyncio.run(get_kanye_quote_coro())

    duration = time() - start_time
    print(f"asyncio, aiohttp and tasks: {duration} seconds")


# ---------------------------------------------- asyncio and loops -----------------------------------------------------
def via_asyncio_loops():
    import asyncio
    import requests

    start_time = time()

    tasks = []
    async def get_kanye_quotes():
        for _ in range(10):
            response = requests.get(url=URL)
            response.raise_for_status()
            print(response.json())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_kanye_quotes())
    loop.close()

    duration = time() - start_time
    print(f"asyncio and loops: {duration} seconds")

# -------------------------------------------- aiohttp and threading ---------------------------------------------------


# -------------------------------------- aiohttp with concurrency(task switching) --------------------------------------


# ----------------------------------------- Running all functions synchronously ----------------------------------------


# ----------------------------------------- Running all functions using threading --------------------------------------