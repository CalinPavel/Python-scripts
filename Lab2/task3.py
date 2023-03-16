#!/usr/bin/env python

import threading
import random

"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""

class Coffee:
    """ Base class """

    def __init__(self,name,size):
        self.name=name
        self.size=size

    def get_name(self):
        """ Returns the coffee name """
        return self.name

    def get_size(self):
        """ Returns the coffee size """
        return self.size

class Americano(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        Coffee.__init__(self,"Americano","small")

class Espresso(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        Coffee.__init__(self,"Espresso","long")


class Cappuccino(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        Coffee.__init__(self,"Cappuccino","medium")
    

class CoffeeFactory():
    def __init__(self, current_buffer , id):

        self.id = id
        self.buffer = current_buffer

    def pick_coffee(self):
        coffee= ["espresso" , "cappuccino" , "americano"]
        return coffee[random.randint(0, 2)]

    def produce(self):
        while True:
            coffe_type=self.pick_coffee()

            # print(coffe_type)

            if(coffe_type == "espresso"):
                my_coffee = Espresso("large")
            
            if(coffe_type == "cappuccino"):
                my_coffee = Cappuccino("medium")
            
            if(coffe_type == "americano"):
                my_coffee = Americano("small")

            print(f"Factory {self.id} produced {coffe_type} {my_coffee.get_size()}")
            
            self.buffer.put(my_coffee.get_name())

class User:

    def __init__(self, buffer ,id):
        self.id = id
        self.buffer = buffer
    
    def consume(self):
        while True:
            item = self.buffer.get()
            print(f"Consumer {self.id} consumed {item}")

class Distribuitor:

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

        self.mutex = threading.Lock()

        self.empty = threading.Semaphore(self.capacity)
        self.full = threading.Semaphore(0)

    def put(self, item):
        self.empty.acquire()
        self.mutex.acquire()

        self.buffer.append(item)

        # print(f"Produced {item}")

        self.mutex.release()
        self.full.release()

    def get(self):
        self.full.acquire()
        self.mutex.acquire()
        item = self.buffer.pop(0)
        # print(f"Consumed {item}")
        self.mutex.release()
        self.empty.release()
        return item


def main():

    capacity = int(input("Enter factory capacity: "))
    num_producers = int(input("Enter number of producers: "))
    num_consumers = int(input("Enter number of consumers: "))

    threads_consumer = []
    threads_producer = []

    current_buffer = Distribuitor(capacity)

    for i in range(0,num_producers):
        current_producer = CoffeeFactory(current_buffer,i)
        thread = threading.Thread(target=current_producer.produce, args=())
        threads_producer.append(thread)
        thread.start()

    for i in range(0,num_consumers):
        current_consumers = User(current_buffer,i)
        thread = threading.Thread(target=current_consumers.consume, args=())
        threads_consumer.append(thread)
        thread.start()


    for thread in threads_consumer:
        thread.join()

    for thread in threads_producer:
        thread.join()


if __name__ == "__main__":
    main()
