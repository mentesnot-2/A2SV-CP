class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        mx_time = 0
        p_time = 0
        t_time = len(tasks) - 1

        while t_time >= 0 and p_time < len(processorTime):
            mx_time = max(mx_time,processorTime[p_time] + tasks[t_time])
            t_time-=4
            p_time+=1
        return mx_time
        
        