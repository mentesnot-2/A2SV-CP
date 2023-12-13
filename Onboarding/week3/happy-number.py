class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        st=set()
        while (1):
            n = str(n)
            sm = 0
            for i in n:
                sm+=(int(i)**2)
            n = sm
            
            if (n == 1):
                return True
            if n in st:
                return False
            st.add(n)
        