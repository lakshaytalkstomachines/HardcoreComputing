"""
    Given an input of N integers find the numbers which are divisible by K

    TC:
        7 3
        1
        51
        966369
        7
        9
        999996
        11 
"""
# First line of input is the values of n, k

# consume input
n, k = map(int, input().split())

count = 0
for i in range(n):
    number = int(input())
    if number % k == 0:
        count = count + 1

print(count)
    

