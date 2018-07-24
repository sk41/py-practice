import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

def measure_time_decor(func):
    """
     find time taken by function to run
    :param func:
    :return:
    """
    # Nested function
    def wrap():
        start=time.time()
        func()
        end=time.time()
        logging.debug("time taken to run the {}() is {}".format(func.__name__,end-start))
    #decorator returns function
    return wrap

@measure_time_decor
def display():
    """
    summation of numbers from 1 to given range
    :return:
    """
    n=int(input("Enter the number:"))
    sum=0
    for i in range(n):
        sum+=i
    logging.debug("summation of 1 to {} = {}".format(n,sum))

display()


