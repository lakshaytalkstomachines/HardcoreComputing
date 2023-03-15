"""
  Given two numbers A and B, find the relation between them ie. relational operation.
  They can be only ">", "<", "="
"""

total_test_cases = int(input())

for _ in range(total_test_cases):
    first_num, second_num = map(int, input().split(" "))
    if first_num == second_num:
        print("=")
    elif first_num < second_num:
        print("<")
    elif first_num > second_num:
        print(">")