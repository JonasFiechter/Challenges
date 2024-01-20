'''
Code Testing Challenge: Longest Consecutive Sequence

Problem Statement:

Given an unsorted array of integers, find the length of the longest consecutive 
elements sequence.

Write a Python function longest_consecutive_sequence(nums) to solve this problem

Sample Parameters:

    Test cases with varying input lists.

Example:

python

nums1 = [100, 4, 200, 1, 3, 2]
# Output: 4 (Explanation: The longest consecutive sequence is [1, 2, 3, 4].)

nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9 (Explanation: The longest consecutive sequence is 
    [0, 1, 2, 3, 4, 5, 6, 7, 8].)

Feel free to take your time to solve this problem. Once you have a solution, you 
can compare it with the one I provide. If you have any questions or need further 
clarification, feel free to ask!
'''

def longest_consecutive_sequence(nums):
    output = []
    final_output = []

    # find the minor and sort
    for index in range(len(nums) + 1):
        print(index, output)
        if nums:
            minor = min(nums)
            nums.remove(minor)
            if minor not in output:
                output.append(minor)

    previous_num = min(output)
    final_output.append(previous_num)
    for num in output[1::]:
        print(f'Calc - {previous_num} {num}')
        if (num - previous_num) != 1:
            print('Inside if')
            return final_output
        final_output.append(num)
        previous_num = num

    return final_output


if __name__ == '__main__':
    nums1 = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive_sequence(nums1))

    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longest_consecutive_sequence(nums2))