class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original = str(x)
        if str(x) == original[::-1]:
            return True
        else:
            return False
    

