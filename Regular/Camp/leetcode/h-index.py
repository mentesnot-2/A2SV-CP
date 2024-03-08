class Solution:
    def hIndex(self, citations: List[int]) -> int:

        def hasAtLeastHPapersWithHCitations(h, citations):
            return sum(cite_count >= h for cite_count in citations) >= h

        low = 0
        high = len(citations)
        while low <= high:
            mid = (low + high) // 2;
            if hasAtLeastHPapersWithHCitations(mid, citations):
                low = mid + 1;
            else:
                high = mid - 1;
        return high