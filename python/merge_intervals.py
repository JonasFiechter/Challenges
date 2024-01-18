'''
Certainly! Here's a coding challenge for you:

### Challenge: Merge Intervals


You are given a list of intervals, where each interval consists of a start and 
end time. Your task is to merge overlapping intervals.

Write a Python function `merge_intervals(intervals)` that takes a list of 
intervals as input and returns a new list of merged intervals.

#### Example:

```python
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]

# Output: [(1, 6), (8, 10), (15, 18)]
```

#### Explanation:

- The intervals (1, 3) and (2, 6) overlap, so they are merged into (1, 6).
- The interval (8, 10) is not overlapping with any other interval, so it remains 
unchanged.
- The interval (15, 18) is not overlapping with any other interval, so it 
remains unchanged.

#### Constraints:

- The input list of intervals is non-empty and contains only positive integers.
- The start time of each interval is less than or equal to the end time.

Feel free to take your time to solve this problem. Once you have a solution, you 
can compare it with the one I provide. If you have any questions or need further 
clarification, feel free to ask!
'''

def merge_intervals(intervals: list):

    for index, curr_interval in enumerate(intervals):
        # Compare with next
        for sec_interval in intervals[index+1:]:
            if curr_interval[1] > sec_interval[0]:
                curr_interval = (curr_interval[0], sec_interval[1])
                intervals[index] = curr_interval
                intervals.pop(index+1)
    print(intervals)


if __name__ == '__main__':
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    intervals = [(2, 3), (2, 6), (8, 10), (15, 18)]
    merge_intervals(intervals)