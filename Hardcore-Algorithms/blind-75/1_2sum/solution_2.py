from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    some_map = {}
    for index, element in enumerate(nums):
        diff = target - element
        if element in some_map:
            return [index,some_map[element]]
        some_map[diff] = index