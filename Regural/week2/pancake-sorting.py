class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        final = []
        for i in range( n, 0, -1):
            indx = arr.index(i)
            arr[: indx + 1] = arr[: indx + 1][::-1]
            arr[:i] = arr[: i][::-1]
            final.append(indx + 1)
            final.append(i)
        return final
            