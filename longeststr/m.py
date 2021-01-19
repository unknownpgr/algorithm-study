class Solution(object):
    def lengthOfLongestSubstring(self, st):
        """
        :type s: str
        :rtype: int
        """
        l = len(st)
        if l < 2:
            return l
        la = {st[0]: 0}
        av = 0
        ml = 0
        for i in range(1, l):
            if st[i] in la:
                av = max(av, la[st[i]]+1)
            la[st[i]] = i
            if (i-av) > ml:
                ml = i-av
        return ml+1
