"""
  Given a number, print the reverse of the number
"""
total_test_cases = int(input())

for _ in range(total_test_cases):
    number = int(input())
    new_number = 0
    while number:
        rem = number % 10
        new_number = new_number * 10 + rem
        number = int(number/10)
    print(new_number)
