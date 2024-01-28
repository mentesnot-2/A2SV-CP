class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        first_ptr = 0
        secnd_ptr = 0

        while first_ptr < len(name):
            char = name[first_ptr]
            cnt = 0
            while first_ptr < len(name) and name[first_ptr] == char:
                first_ptr+=1
                cnt+=1
            count = 0
            while secnd_ptr < len(typed) and typed[secnd_ptr] == char:
                count+=1
                secnd_ptr+=1

            if count < cnt:
                return False
        return True if secnd_ptr >= len(typed) else False
        
        