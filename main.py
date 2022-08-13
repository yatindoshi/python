# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

import numpy
import numpy as np
import pandas as pd
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def data_frame_usage():
    numbers = np.array(range(0, 11))
    squares = numbers ** 2
    df = pd.DataFrame({'numbers': numbers, 'squares': squares})
    print(df)


def factorial(number):
    return np.prod(np.arange(1, number + 1))


def dot_product(a, b):
    if not isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
        raise Exception("inputs should be numpy arrays")
    if len(a) != len(b):
        raise Exception("both vectors should be of same size")
    return sum(a * b)


def fibonacci(n):
    fib = np.array([0, 1])
    for i in range(2, n):
        next_fib = fib[i - 1] + fib[i - 2]
        fib = np.append(fib, next_fib)
    return fib


def usage_of_zip():
    names = ['arun', 'yatin']
    values = [40, 35]
    d = dict(zip(names, values))
    return d


def initialize1():
    start_time = time.perf_counter()
    N = 10000
    numbers = np.zeros(N)
    for i in range(N):
        numbers[i] = i ** 2
    end_time = time.perf_counter()
    return end_time - start_time


def initialize2():
    start_time = time.perf_counter()
    N = 10000
    numbers = np.full(N, 0)
    for i in range(N):
        numbers = np.append(numbers, i ** 2)
    end_time = time.perf_counter()
    return end_time - start_time


def initialize3():
    start_time = time.perf_counter()
    N = 10000
    numbers = []
    for i in range(N):
        numbers.append(i ** 2)
    end_time = time.perf_counter()
    return end_time - start_time


def poisson_number(n):
    counter = 0
    current_val = 1
    while current_val >= numpy.exp(-n):
        current_val = current_val * random.uniform(0, 1)
        counter = counter + 1
    return counter


def np_broadcast():
    vector = np.arange(9)
    print(vector)
    matrix = np.reshape(vector, (3, 3))
    print(matrix)
    repeated_matrix = np.tile(matrix, (3, 1))
    print(repeated_matrix)
    converted_column_vector = np.reshape(vector, (len(vector), 1))
    print(converted_column_vector)
    multiplication_matrix = repeated_matrix * converted_column_vector
    print(multiplication_matrix)


# print(initialize1())
# print(initialize2())
# print(initialize3())
# print(poisson_number(10)
np_broadcast()
