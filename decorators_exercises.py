# 1. Decorators - simple decorator
import functools
from math import fsum
from time import perf_counter, sleep


def example_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print(f"Now calling {func.__name__}...")
        func()
        print(f"{func.__name__} has ended.")

    return wrapper


@example_decorator
def example():
    print('Printing from inside of original example() function')


@example_decorator
def greeter():
    print("Hello!")


example()
print()
greeter()
print()


def hello(func):
    @functools.wraps(func)
    def wrapper():
        print('Hello')
        func()

    return wrapper


@hello
def name():
    print('Alice')


name()


def dispaly(func):
    @functools.wraps(func)
    def wrapper():
        print('The current user is: ', end='')
        func()

    return wrapper


@dispaly
def who():
    print('Alice')


who()


# 2. Decorators - decorators with arguments
def pretty_sum_ab(func):
    @functools.wraps(func)
    def wrapper(a, b):
        print(f'{str(a)} + {str(b)} is: ', end='')
        return func(a, b)

    return wrapper


@pretty_sum_ab
def sum_ab(a, b):
    summed = a + b
    print(summed)


sum_ab(5, 3)


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args):
        t = perf_counter()
        result = func(*args)
        print("Function took " + str(perf_counter() - t) + " seconds to run")
        return result

    return wrapper


@measure_time
def my_function(n):
    sleep(n)
    return 'This is the return on the original function'


# print(my_function(1))
print()


#######################
# A real world example #

# V1
def stopwatch(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        stop_time = perf_counter()

        print(f"{func.__name__} ran in {stop_time - start_time:.5f}s")

    return wrapper


@stopwatch
def make_list(size):
    return list(range(size))


@stopwatch
def make_set(size):
    return set(range(size))


make_list(100_000)
make_set(100_000)
print()


# V2 with average

def stopwatch(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        times = []

        for _ in range(10):
            start_time = perf_counter()
            func(*args, **kwargs)
            stop_time = perf_counter()

            elapsed = stop_time - start_time
            times.append(elapsed)

        average_time = fsum(times) / len(times)

        print(f"{func.__name__} ran in {average_time:.5f}s on average")

    return wrapper


@stopwatch
def make_list_average(size):
    return list(range(size))


@stopwatch
def make_set_average(size):
    return set(range(size))


make_list_average(100_000)
make_set_average(100_000)
