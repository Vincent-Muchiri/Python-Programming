import requests
import asyncio
import aiohttp
from pprint import pprint

number = 0


POKEMON_ENDPOINT = f"https://pokeapi.co/api/v2/pokemon/{number}"
KANYE_QUOTES_ENDPOINT = "https://api.kanye.rest"


def run_fns_without_Session():
    async def get_pokemon(number):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}")
        pokemon = response.json()
        return pokemon['name']

    async def get_kanye_quote():
        response = requests.get(KANYE_QUOTES_ENDPOINT)
        kanye_quote = response.json()
        return kanye_quote['quote']

    loop = asyncio.get_event_loop()

    group1 = asyncio.gather(*[get_pokemon(number) for number in range(1, 50)])
    group2 = asyncio.gather(*[get_kanye_quote() for _ in range(1, 50)])

    all_groups = asyncio.gather(group1, group2)

    results = loop.run_until_complete(all_groups)

    loop.close()

    pprint(results)


# def run_fns_session():
#     async def get_pokemon(session, url):
#         async with session.get(url) as response:
#             pokemon = await response.json()
#             return pokemon['name']
#
#     async def get_kanye_quote(session, url):
#         async with session.get(url) as response:
#             kanye_quote = await response.json()
#             return kanye_quote['quote']
#
#     async with aiohttp.ClientSession() as session:
#         loop = asyncio.get_event_loop()
#
#         group1 = asyncio.gather(*[get_pokemon(session, POKEMON_ENDPOINT.format(number)) for number in range(1, 10)])
#         group2 = asyncio.gather(*[get_kanye_quote(session, KANYE_QUOTES_ENDPOINT) for _ in range(1, 10)])
#
#         all_groups = asyncio.gather(group1, group2)
#
#         results = loop.run_until_complete(all_groups)
#
#         loop.close()
#
#         pprint(results)



