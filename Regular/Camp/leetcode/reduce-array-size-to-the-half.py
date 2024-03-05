class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) // 2
        cnt = Counter(arr)
        ar = [i for i in cnt.values()]
        if len(ar) == 1:
            return 1
        if len(ar) == len(arr):
            return len(ar) // 2
        ar.sort(reverse=True)
        for i in range(1,len(ar)):
            ar[i] = ar[i] + ar[i -1]
        for j in range(len(ar)):
            if ar[j] >= half:
                return j + 1