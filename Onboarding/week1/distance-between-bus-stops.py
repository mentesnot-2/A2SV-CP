class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """

        n = len(distance)
        tot = sum(distance)
        sm1 = 0
        if start > destination:
            sm1 = sum(distance[destination:start ])
        else:
            sm1 = sum(distance[start:destination])
        
        return min(sm1,tot - sm1)
        