class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        n = len(spells)
        l = len(potions)
        p = [None] * n
        potions.sort()
        for i in range(n):
            m = spells[i]
            left = 0
            right = l-1
            while left <= right:
                mid = left + (right - left)//2
                product = m * potions[mid]
                if product <success:
                    left = mid + 1
                else:
                    right = mid - 1
            p[i] = l - left
        return p