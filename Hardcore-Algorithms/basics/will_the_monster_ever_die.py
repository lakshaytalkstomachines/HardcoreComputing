"""
    A monster has health 'H'. 
        Every time we hit the monster , it loses health 'X'
        But it also gains health 'Y', right before we hit.
    
        Given H, X, Y, find if the monster will ever die.
              Print 1, if dies,
              Print 0, if it does not.
"""

num_of_test_cases = int(input())

for _ in range(num_of_test_cases):
    h, x, y = map(int, input().split())

    # if x is less than or equal to y,
    #  then the monster will never die as it will always gain 
    #  health as at least as much as it will lose.
    if x <= y :
        print(0)
    else: 
        print(1)