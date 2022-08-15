url = "https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/"


import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

COUNT = 200000000
SLEEP = 10


def io_bound(sec):

    # TODO Get the current process id
    pid = os.getpid()

    # TODO Get the name
    thread_Name = current_thread().name
    process_Name = current_process().name

    print(f"{pid} * {process_Name} * {thread_Name}")

    time.sleep(sec)

    print(f"{pid} * {process_Name} * {thread_Name}")

def cpu_bound(n):
    pid = os.getpid()

    thread_Name = current_thread().name
    process_Name = current_process().name

    print(f"{pid} * {process_Name} * {thread_Name}")

    while n > 0:
        n -= 1

    print(f"{pid} * {process_Name} * {thread_Name}")

# TODO Calculate the time
if __name__ == "__main__":
    # start = time.time()
    #
    # # TODO Measure the time to run the processes normally
    # io_bound(SLEEP)
    # io_bound(SLEEP)
    #
    # end = time.time()
    # print("Time taken in seconds -", end - start)

    # TODO Making use of threading to run the io_bound task twice
    # start = time.time()
    #
    # t1 = Thread(target=io_bound, args=(SLEEP,))
    # t2 = Thread(target=io_bound, args=(SLEEP,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    #
    # end = time.time()
    # print("Time taken in seconds -", end - start)

    # TODO Running CPU-bound task twice one after another
    # start = time.time()
    #
    # cpu_bound(COUNT)
    # cpu_bound(COUNT)
    #
    # end = time.time()
    # print("Time taken in seconds -", end - start)

    # TODO Threading doesn't work for CPU-bound tasks
    start = time.time()

    t1 = Thread(target=cpu_bound, args=(COUNT,))
    t2 = Thread(target=cpu_bound, args=(COUNT,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.time()
    print("Time taken in seconds -", end - start)



