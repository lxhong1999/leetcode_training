class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}
        right = 0
        left = 0
        res = 0
        ll = len(s)
        while (right<ll):
            c = s[right]
            right = right + 1
            window[c] = window.setdefault(c,0) + 1

            while (window[c]>1):
                d = s[left]
                print(d)
                left = left+1
                window[d] = window[d] - 1 
            res = max(res, right-left)
        return res