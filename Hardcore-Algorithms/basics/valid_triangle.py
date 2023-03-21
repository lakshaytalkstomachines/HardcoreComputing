"""
    Given 3 angles, find if they form a valid triangle.
"""

num_of_test_cases = int(input())

for _ in range(num_of_test_cases):
    angle_a, angle_b, angle_c = map(int, input().split())

    if angle_a + angle_b + angle_c == 180:
        print("YES")
    else:
        print("NO")
    