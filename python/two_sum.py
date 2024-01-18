'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

'''

def two_sum_3(sums:list, target:int):
    for index, number in enumerate(sums):
        for i, sub_number in enumerate(sums):
            if index == i:
                break
            else:
                if number + sub_number == target:
                    return [index, i]





if __name__ == '__main__':
    print(two_sum_3([2,7,11,15], 9))
    print(two_sum_3([3,3], target = 6))












# Brute Force
def two_sum(nums: list, target: int):
    for x in range(len(nums)):
        for y in range(len(nums)):
            if x != y:
                if nums[x] + nums[y] == target:
                    return [x, y]


l = [i + 1 for i in range(129)]
# print(two_sum(l, 251))


def two_sum_2(nums: list, target):
    for i, n in enumerate(nums):
        rest = target - n
        if rest in nums and nums.index(rest) != i:
            return [i, nums.index(rest)]

# print(two_sum_2([3,2,4], 6))