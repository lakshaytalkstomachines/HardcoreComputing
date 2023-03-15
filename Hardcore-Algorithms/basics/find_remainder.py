"""
    Given two number A and B, print the remainder
"""

number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    first_num, second_num = map(int, input().split())
    print(first_num % second_num)
    