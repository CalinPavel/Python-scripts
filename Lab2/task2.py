#!/usr/bin/env python

"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""

import threading

def print_number(num):
    print(f"thread {threading.current_thread().name} - argument:{num}")            


def main():

    threads = []

    for i in range(1, 11):
        thread = threading.Thread(target=print_number, args=(i,), name=f"Thread-{i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
