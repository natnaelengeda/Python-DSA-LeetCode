# Two Sum

from typing import List

# nums = [2,7,11,15]
nums = [3,2,3]
target = 6

# My Solution
def twoSum(nums: List[int], target:int):

  for i, x in enumerate(nums):
    for j, y in enumerate(nums):
      if i!= j:
        if x+y == target:
          return [i,j]

# Optimal Solution
def twoSumOptimal(nums: List[int], target:int) -> List[int]:
  # Hash Set
  seen = {}

  for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
    print(seen)

print(twoSumOptimal(nums, target))

