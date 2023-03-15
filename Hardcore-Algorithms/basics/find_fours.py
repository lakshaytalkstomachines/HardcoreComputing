"""
    Given a number, find the number of occurrences of number 4
"""

number_to_find = 4
total_test_cases = int(input())

for _ in range(total_test_cases):
    number = int(input())
    frequency = 0

    while(number):
        rem = number % 10
        if rem == number_to_find:
            frequency = frequency + 1
        number = int(number /10)
    
    print(frequency)
    