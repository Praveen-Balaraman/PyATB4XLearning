from time import time


def mydecorator(func):
    print("Test is started")
    t=time()
    print(t)
    func()
    print("Test is Ended")

@mydecorator
def testing():
    print("Testing is in progress")