class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        freq = Counter()
        min_val = float('inf')

        for a in basket1:
            freq[a] += 1
            min_val = min(min_val, a)
        for b in basket2:
            freq[b] -= 1
            min_val = min(min_val, b)

        excess = []
        for val, count in freq.items():
            if count % 2 != 0:
                return -1
            excess.extend([val] * (abs(count) // 2))

        excess.sort()
        cost = 0
        for i in range(len(excess) // 2):
            cost += min(excess[i], 2 * min_val)

        return cost