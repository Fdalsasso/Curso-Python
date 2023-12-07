import sched
import time

s = sched.scheduler(time.time, time.sleep)

def print_time (a = "default"):
    print(time.time(), a)


def print_kevin ():
    s.enter(2, 1 ,print_time, argument=("kevin"))
    s.run()


print_kevin()

def imprimir_gusty ():
    s.enter(3, 2 ,print_time, argument=("Gus was here"))
    s.run()

imprimir_gusty()

#print_some_times()
def imprimoCualquiera():
    print("\nCualquiera")

def funcionCualquiera ():
    s.enter(10, 1, imprimoCualquiera)
    s.run()

funcionCualquiera()

def print_mensaje ():
    s.enter(3, 1, print_time, argument=("Funciona!!",))
    s.enter(3, 2, print_time, argument=("No, mentira",))
    s.enter(5, 3, print_time, argument=("x_x",))
    s.run()

print_mensaje()
