class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans=[]
        maximum=max(candies)
        for candy in candies:
            if candy+extraCandies>=maximum:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        