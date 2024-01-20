'''
Code Testing Challenge: Merge Intervals

Problem Statement:

Given a list of intervals represented by pairs of integers [start, end], merge 
overlapping intervals.

Write a Python function merge_intervals(intervals) to solve this problem.

Sample Parameters:

    Test cases with varying input lists of intervals.

Example:

python

intervals1 = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]] (Explanation: Merge [1,3] and [2,6].)

intervals2 = [[1,4],[4,5]]
# Output: [[1,5]] (Explanation: Merge [1,4] and [4,5].)
'''

def merge_intervals(intervals:list):
    output = []

    while True:
        if not intervals:
            return output

        if len(intervals) > 1:
            interval, next_interval = intervals.pop(0), intervals.pop(0)
        else:
            interval = intervals.pop()

        if next_interval:
            # Check, merge and add to output
            if interval[-1] >= next_interval[0]:
                merged = [interval[0], next_interval[-1]]
                output.append(merged)
            else:
                output.append(interval)
                output.append(next_interval)
        
        else:
        # Just add current interval
            output.append(interval)
        

if __name__ == '__main__':
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
    print(merge_intervals([[1,4],[4,5]]))
    # Test Case 1
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
    # Expected Output: [[1, 6], [8, 10], [15, 18]]

    # Test Case 2
    print(merge_intervals([[1,4],[4,5]]))
    # Expected Output: [[1, 5]]

    # Test Case 3
    print(merge_intervals([[1,2],[3,4],[5,6]]))
    # Expected Output: [[1, 2], [3, 4], [5, 6]]

    # Test Case 4
    print(merge_intervals([[1,3],[2,4],[5,7]]))
    # Expected Output: [[1, 4], [5, 7]]

    # Test Case 5
    print(merge_intervals([[1,5],[2,3],[4,7],[8,10],[12,15]]))
    # Expected Output: [[1, 7], [8, 10], [12, 15]]
