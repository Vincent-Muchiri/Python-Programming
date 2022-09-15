import concurrent.futures
from time import time
import requests
from pprint import pprint


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


# ------------------------------------------ Synchronous : Request library ---------------------------------------------
def via_synchronous():
    start = time()
    for _ in range(10):
        get_kanye_quote()

    stop = time()
    duration = stop - start
    print(f"The program ran synchronously for {duration} seconds")


# via_synchronous()


# The program ran synchronously for 4.9016804695129395 seconds
# The program ran synchronously for 5.154052972793579 seconds
# The program ran synchronously for 4.864717960357666 seconds
# The program ran synchronously for 5.012331962585449 seconds
# The program ran synchronously for 6.6834070682525635 seconds
# The program ran synchronously for 4.955312013626099 seconds


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


# via_threading_module()


# The functions ran via the threading module for 0.7083132266998291 seconds
# The functions ran via the threading module for 0.5660810470581055 seconds
# The functions ran via the threading module for 2.305131673812866 seconds
# The functions ran via the threading module for 0.8787283897399902 seconds
# The functions ran via the threading module for 0.6732206344604492 seconds
# The functions ran via the threading module for 0.6277730464935303 seconds


# ------------------------------- Threading using the ThreadPoolExecutor and submit()-----------------------------------
def via_threadpool_submit():
    from concurrent.futures import ThreadPoolExecutor

    start = time()
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(10):
            f = executor.submit(get_kanye_quote)
            futures.append(f)

        for future in concurrent.futures.as_completed(futures):
            future.result()

    duration = time() - start
    print(f"The functions ran via ThreadPoolExecutor class and submit method for {duration} seconds")


# via_threadpool_submit()


# The functions ran via ThreadPoolExecutor class and submit method for 0.8991448879241943 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 0.8566598892211914 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 0.76261305809021 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 0.8509018421173096 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 1.4758570194244385 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 1.3589391708374023 seconds


# ------------------------------- Threading using the ThreadPoolExecutor and map()-----------------------------------
def via_threadpool_map():
    from concurrent.futures import ThreadPoolExecutor

    start = time()
    futures = []
    limit = [10]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(get_kanye_quote_map, limit)

    duration = time() - start
    print(f"The functions ran via ThreadPoolExecutor class and map method for {duration} seconds")


# via_threadpool_map()
# The functions ran via ThreadPoolExecutor class and map method for 6.595656633377075 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.512631177902222 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.567673444747925 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.274266958236694 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.628472089767456 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.308933734893799 seconds


# --------------------------------------------------- Results ----------------------------------------------------------
# The program ran synchronously for 6.496086597442627 seconds
# The functions ran via the threading module for 0.9808788299560547 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 1.7972912788391113 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.183596849441528 seconds

# The program ran synchronously for 6.819275140762329 seconds
# The functions ran via the threading module for 1.2086169719696045 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 1.1898632049560547 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.494396448135376 seconds

# The program ran synchronously for 6.1955931186676025 seconds
# The functions ran via the threading module for 0.9303243160247803 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 1.7626781463623047 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.414564609527588 seconds

# The program ran synchronously for 6.35685920715332 seconds
# The functions ran via the threading module for 1.219437599182129 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 0.6262671947479248 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.283244371414185 seconds

# The program ran synchronously for 7.579585075378418 seconds
# The functions ran via the threading module for 1.0328800678253174 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 0.887213945388794 seconds
# The functions ran via ThreadPoolExecutor class and map method for 6.19865608215332 seconds

# The program ran synchronously for 6.8567516803741455 seconds
# The functions ran via the threading module for 1.8672411441802979 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 1.0114271640777588 seconds
# The functions ran via ThreadPoolExecutor class and map method for 7.979430913925171 seconds

# The program ran synchronously for 5.4259679317474365 seconds
# The functions ran via the threading module for 0.9085221290588379 seconds
# The functions ran via ThreadPoolExecutor class and submit method for 0.5295825004577637 seconds
# The functions ran via ThreadPoolExecutor class and map method for 5.614346742630005 seconds


# ---------------------------------------- Running Threads within Threads ? --------------------------------------------

def get_pokemon2(number, session):
    response = session.get(f"https://pokeapi.co/api/v2/pokemon/{number}")
    pokemon = response.json()
    return pokemon['name']


def get_kanye_quote2(session):
    response = session.get("https://api.kanye.rest")
    kanye_quote = response.json()
    return kanye_quote['quote']

def run_multiple_fns():
    with requests.Session() as session:
        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            futures = []
            # get_pokemon_tasks = [executor.submit(get_pokemon2, number, session) for number in range(0, 15)]
            get_kanye_quote_tasks = [executor.submit(get_kanye_quote2, session) for _ in range(0, 15)]
            get_kanye_quote_tasks2 = [executor.submit(get_kanye_quote2, session) for _ in range(0, 15)]

            futures = get_kanye_quote_tasks + get_kanye_quote_tasks2

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(result)

run_multiple_fns()
# via_threadpool_submit()
# futures = []
# with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     for _ in range(10):
#         f = executor.submit(get_kanye_quote)
#         futures.append(f)
#
#     for future in concurrent.futures.as_completed(futures):
#         print(future.result())