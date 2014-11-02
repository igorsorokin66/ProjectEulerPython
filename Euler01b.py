__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Solved with no data structures'

sum_of_multiples_of_3_under_1000 = 0
for multiple_of_3 in range(3, 1000, 3):
    sum_of_multiples_of_3_under_1000 += multiple_of_3
#print(sum_of_multiples_of_3_under_1000)

sum_of_multiples_of_5_under_1000_not_divisible_by_3 = 0
for multiple_of_5 in range(5, 1000, 5):
    if multiple_of_5 % 3 != 0:
    #checks that its not divisible by 3
        sum_of_multiples_of_5_under_1000_not_divisible_by_3 += multiple_of_5
#print(sum_of_multiples_of_5_under_1000_not_divisible_by_3)

sum_of_multiples_of_3_and_5_under_1000 = 0
sum_of_multiples_of_3_and_5_under_1000 += sum_of_multiples_of_3_under_1000
sum_of_multiples_of_3_and_5_under_1000 += sum_of_multiples_of_5_under_1000_not_divisible_by_3
print(sum_of_multiples_of_3_and_5_under_1000)