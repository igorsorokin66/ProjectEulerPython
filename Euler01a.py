__author__ = 'Igor'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Solved using Sets'

def generate_list_of_multiples(start, end, increment):
    list_of_multiples = [i for i in range(start, end, increment)]
    return list_of_multiples

list_of_multiples_of_3_under_1000 = generate_list_of_multiples(3, 1000, 3)
#print(list_of_multiples_of_3_under_1000)
list_of_multiples_of_5_under_1000 = generate_list_of_multiples(5, 1000, 5)
#print(list_of_multiples_of_5_under_1000)

set_of_multiples_of_3_under_1000 = set(list_of_multiples_of_3_under_1000)
set_of_multiples_of_5_under_1000 = set(list_of_multiples_of_5_under_1000)
union_of_multiples_of_3_and_5_under_1000 = set_of_multiples_of_3_under_1000.union(set_of_multiples_of_5_under_1000)
sum_of_union_of_multiples_of_3_and_5_under_1000 = sum(union_of_multiples_of_3_and_5_under_1000)
print(sum_of_union_of_multiples_of_3_and_5_under_1000)