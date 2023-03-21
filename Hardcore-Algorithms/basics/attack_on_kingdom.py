"""
   Given an array of temperatures, find the second coldest night
     for the kind to attack on kingdom.
"""

num_of_test_cases = int(input())
for _ in range(num_of_test_cases):
    num_of_days = int(input())
    temp = list(map(int, input().split()))

    smallest = 0
    small = 0

    if temp[0] <= temp[1]:
        smallest = temp[0]
        small = temp[1]
    else:
        smallest = temp[1]
        small = temp[0]
    
    for t in temp:
        if t < smallest:
            small = smallest
            smallest = t
        elif t < small and t > smallest:
            small = t

    print(small) 