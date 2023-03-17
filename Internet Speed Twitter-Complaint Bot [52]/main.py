from internetSpeedTwitterBot import InternetSpeedTwitterBot
from concurrent.futures import as_completed, ThreadPoolExecutor
from pprint import pprint

bot = InternetSpeedTwitterBot()


# TODO Run multiple tests concurrently

def test_multiple_times():
    futures, download_speeds_array, upload_speeds_array = [], [], []

    with ThreadPoolExecutor(max_workers=3) as executor:
        for tests in range(3):
            f = executor.submit(bot.get_internet_speed)
            futures.append(f)

    print(len(futures))

    for future in as_completed(futures):
        # TODO Get the speeds
        internet_speed_dict = future.result()

        download_speeds = internet_speed_dict['download_speed']
        download_units = internet_speed_dict['download_units']
        upload_speeds = internet_speed_dict['upload_speed']
        upload_units = internet_speed_dict['upload_units']

        # TODO Convert all speeds to Kbps
        if download_units == "Mbps":
            download_speeds = download_speeds * 1000
        if upload_units == "Mbps":
            upload_speeds = upload_speeds * 1000

        # TODO Append the speeds to a list
        download_speeds_array.append(download_speeds)
        upload_speeds_array.append(upload_speeds)

    print(download_speeds_array)
    print(upload_speeds_array)

    # TODO Check whether there's a speed that is way off and remove it

    # TODO Calculate the average speed

def test_ones():
    internet_speed_dict = bot.get_internet_speed()
    pprint(internet_speed_dict)

