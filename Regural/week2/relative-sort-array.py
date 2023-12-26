class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr=Counter(arr1)
        arr3=[]
        for i in arr2:
            for j in range(arr[i]):
                arr3.append(i)
            arr.pop(i)
        rel=sorted(arr)
        for i in rel:
            for j in range(arr[i]):
                arr3.append(i)
        return arr3