class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.order = [0] * self.n
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.order[idKey - 1] = value
        lst = []
        for i in range(idKey-1):
            if self.order[i] == 0:
                return []
        lst.append(value)
        i = idKey
        while i < self.n and self.order[i] != 0:
            lst.append(self.order[i])
            i+=1
        return lst

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)