# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if intervals is None or len(intervals) == 0:
            return [newInterval]
        results = []
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            results.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval = Interval(
                min(newInterval.start, intervals[i].start),
                max(newInterval.end, intervals[i].end))
            i += 1
        results.append(newInterval)
        results += intervals[i:]
        return results
