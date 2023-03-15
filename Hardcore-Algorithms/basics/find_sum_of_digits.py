"""
    Given a number n, find the sum of all the digits.
"""
total_cases = int(input())

for test_case in range(total_cases):
    total_sum = 0
    for digit in input():
        total_sum = total_sum + int(digit)
    print(total_sum)
