class FrequencyTracker(object):

    def __init__(self):
       
        self.mp = {}
        self.freq = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.mp:
            val = self.mp[number]
            self.freq[val]-=1
            if self.freq[val] == 0:
                del self.freq[val]
            self.mp[number]+=1
            
                
            self.freq[self.mp[number]] = self.freq.get(self.mp[number],0) + 1
        else:
            self.mp[number] = 1
            if 1 in self.freq:
                self.freq[1]+=1
            else:
                self.freq[1] = 1

        
             

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.mp:
            val = self.mp[number]
            self.freq[val]-=1
            if self.freq[val] == 0:
                del self.freq[val]
            self.mp[number]-=1
            if self.mp[number] == 0:
                del self.mp[number]
            if number in self.mp:
                self.freq[self.mp[number]] = self.freq.get(self.mp[number],0) + 1
        
        
    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        print(self.freq)
        print(frequency)
        
        return frequency in self.freq

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)