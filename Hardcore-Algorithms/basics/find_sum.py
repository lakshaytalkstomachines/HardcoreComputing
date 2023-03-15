"""
    Given two number A and B, output the sum of them
"""
total_test_cases = int(input())
for _ in range(total_test_cases):
    first_num, second_num = map(int, input().split(" "))
    print(first_num + second_num)
