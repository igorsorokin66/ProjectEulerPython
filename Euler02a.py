__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Solved using recursion'

def fib(previous_term, next_term, sum_all_even_fibonacci_numbers):
    if previous_term + next_term > 4000000:
        return sum_all_even_fibonacci_numbers
    if (previous_term + next_term) % 2 == 0:
        return fib(next_term, previous_term + next_term, sum_all_even_fibonacci_numbers + previous_term + next_term)
    else:
        return fib(next_term, previous_term + next_term, sum_all_even_fibonacci_numbers)

print(fib(1, 2, 2))