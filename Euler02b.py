__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Solved using a loop'

previous_term = 1
next_term = 2
sum_of_all_even_fibonacci_numbers_under_4_million = 2
under_4_million_flag = True
while under_4_million_flag:
    temporary_storage_of_next_term = next_term
    next_term += previous_term
    previous_term = temporary_storage_of_next_term
    if next_term % 2 == 0:
        sum_of_all_even_fibonacci_numbers_under_4_million += next_term
    if next_term > 4000000:
        under_4_million_flag = False
print(sum_of_all_even_fibonacci_numbers_under_4_million)