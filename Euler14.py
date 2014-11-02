__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Solved using dictonary to keep track of lengths of sequences already computed'


def collatz(number, terms, dict):
    if number in dict.keys():
        return terms + dict[number]
    else:
        if number % 2 == 0:
            return collatz(number / 2, terms + 1, dict)
        else:
            return collatz(number * 3 + 1, terms + 1, dict)

most_amount_of_terms = 0
longest_starting_number = 0
dict = {1: 1}#these magic numbers are because 1 has collatz sequence of 1
for starting_number in range(2, 25):
    answer = collatz(starting_number, 0, dict)
    dict[starting_number] = answer
    if answer > most_amount_of_terms:
        longest_starting_number = starting_number
        most_amount_of_terms = answer
print(longest_starting_number)
print(most_amount_of_terms)