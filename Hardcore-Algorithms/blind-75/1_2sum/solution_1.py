from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(length):
        minor_sum = -1
        first_num = nums[i]
        for j in range(i+1, length):
            second_num = nums[j]
            minor_sum = first_num + second_num
            if minor_sum == target:
                return [i, j]