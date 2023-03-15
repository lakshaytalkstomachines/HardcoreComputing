"""
    Given a number n, find the sum of all the digits.
"""
total_cases = int(input())

for test_case in range(total_cases):
    digits = map(int, input())
    total_sum = sum(digits)
    print(total_sum)
