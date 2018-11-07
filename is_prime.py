#!/usr/bin/env python3

"""
This is a def to check if a number is prime. Works well for numbers under a
million
1 is not prime
All primes except 2 are odd
All promes greater than 3 can be written 6k+/-1
If we cannot find a number <= sqrt(n) that evenly divides n, then n is
the only prime factor of n (n is prime).
"""

from math import sqrt

def is_prime(check_number):
    """ Returns True is factor_of num is prime and False if not """
    if check_number <= 1: # 1 is not prime
        return False

    elif check_number < 4: # 2 and 3 are prime
        return True

    elif check_number % 2 == 0: # evenly divided by 2 not prime
        return False

    elif check_number < 9 == 0: # we have already excluded 4,6,and 8
        return True

    elif check_number % 3 == 0: # evenly divided by 3 not prime
        return False

    else:
        round_sqrt_check_number = int(sqrt(check_number))
        divisor = 5
        while True:
            if check_number % divisor == 0:
                return False
            if check_number % divisor + 2 == 0:
                return False
            divisor += 6
            if divisor >= round_sqrt_check_number:
                break  # number is prime and the final return will give True

    return True

if __name__ == "__main__":

    NUMBER = int(input('Enter number to check for prime: '))

    RESULT = is_prime(NUMBER)

    print(RESULT)
