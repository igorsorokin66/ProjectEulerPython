__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Solved using brute force'

count = 0
import math
max = math.factorial(20)

def prob():
    for i in range(20, max, 20):
        for n in range(11, 20):
            if i % n != 0:
                break
            elif n == 19:
                print(i)
                return
prob()