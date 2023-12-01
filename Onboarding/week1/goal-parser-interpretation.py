class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans = ""
        i = 0
        n = len(command)
        while i < n:
            if command[i] == "G":
                ans+="G"
            elif command[i] == "(":
                if command[i + 1] == ")":
                    ans+="o"
                else:
                    while i < n - 1 and command[i + 1] != ")":
                        ans+=command[i + 1]
                        i = i + 1
            i+=1
        return ans
        