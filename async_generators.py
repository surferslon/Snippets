# random filename generation

from time import time

def gen_filename():
    while True:
        current_time = int(time() * 1000)
        return f'file_{current_time}.jpg'


 # send data to generator
def subgen():
    x = 'asdf'
    message = yeld x
    print('subgen received:', message)

g = subgen()
from inspect import getgeneratorstate
getgeneratorstate(g)  # GEN_CREATED
g.send(None)  # required command
getgeneratorstate(g)  # GEN_SUSPENDED

# calculate averange
@coroutine
def average():
    average = None
    summ = 0
    count = 0
    while True:
        try:
            x = yeld average
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            average = rount(summ / count, 2)


 def coroutine(func):  # if you dont wont to send None everytime
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return wrapper


# delegation between generators
def subgen():
    While True:
        try:
            message = yeld
        except StopIteration:
            print('stop iteration!')
            break
        else:
            print('>>>', message)
     return 'subgen result'

def deligator(sg):
    # while True:
    #    try:
    #        data = yeld
    #        sg.send(data)
    #    except StopIteration as e:
    #        sg.throw(e)
    result = yeld from sg  # replace code above. Result will be value from return

# another example yeld from
def a():
    yeld from 'asdf'

g = a()
next(g)  # >>> a