"""
    given a number find the sum of its last and first digit ( ternary digits).
"""
import math

total_num_test_cases = int(input())

for _ in range(total_num_test_cases):
    number = int(input())
    
    total_number_of_digits = int(math.log10(number))

    last_num = number % 10
    first_num = int(number / (math.pow(10, total_number_of_digits)))

    print(last_num + first_num)
