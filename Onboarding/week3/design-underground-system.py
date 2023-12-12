class UndergroundSystem(object):

    def __init__(self):
        self.checkin = defaultdict(tuple)
        self.tot_time = defaultdict(tuple)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkin[id] = (t,stationName)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationselfName: str
        :type t: int
        :rtype: None
        """
        time,checkin = self.checkin[id]
        if not self.tot_time[checkin+"to"+stationName]:
            self.tot_time[checkin+"to"+stationName] = (0,0)
        tot,cnt = self.tot_time[checkin+"to"+stationName]
        tot+=(t - time)
        self.tot_time[checkin+"to"+stationName] = (tot,cnt+1)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        sm,cnt = self.tot_time[startStation+"to"+endStation]
        
        
        return float(sm) / float(cnt)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)