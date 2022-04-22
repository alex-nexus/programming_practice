from random import random


def estimate_pi(n):
    return 4.0 * sum([in_circle() for i in xrange(n)]) / n


def in_circle():
    x = random()  # 0-1
    y = random()  # 0-1
    return 1 if x * x + y * y < 1 else 0


print estimate_pi(1000000)
