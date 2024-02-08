class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[2])
        arr = [0] * trips[-1][2]
        for i in range(len(trips)):
            passengers,frm,to = trips[i]
            
            arr[frm]+=passengers
            if to != len(arr):
                arr[to]-=passengers
        for k in range(1,len(arr)):
            arr[k]+=arr[k - 1]
        for i in arr:
            if i > capacity:
                return False
        return True
        