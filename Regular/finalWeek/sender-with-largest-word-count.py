class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        countOf = defaultdict(int)

        for i in range(len(messages)):
            val = messages[i].split(" ")
            countOf[senders[i]]+=len(val)
        
        largest = 0
        name = ""
        for key in countOf:
            if countOf[key] > largest:
                largest = countOf[key]
                name = key
            elif countOf[key] == largest:
                if name < key:
                    name = key

            
        return name


       