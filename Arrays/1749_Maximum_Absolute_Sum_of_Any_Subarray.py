class Solution:
    ## Kadane's algorithm
    ## [1,-3,2,3,-4]
    ##  
    ##           -4
    ##         3
    ##       2,5, 1 ==> max = 5
    ##    -3
    ##  1,-2,0
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ## variable to store the local previous max sum
        prevmaxsum = -float(inf)
        ## variable to store the local previous min sum
        prevminsum = float(inf)
        ## variable to store global max sum
        resmaxsum = -float(inf)
        ## variable to store global min sum
        resminsum = float(inf)
        
        for ele in nums:
            ## check if previous max sum with current element is greater than the current element
            ## either consider previous max sum with current element or only curret element
            prevmaxsum = max(prevmaxsum+ele, ele)
            ## check if previous min sum with current element is less than the current element
            ## either consider previous min sum with current element or only curret element
            prevminsum = min(prevminsum+ele, ele)
            ## get global maximum sum so far
            resmaxsum = max(resmaxsum, prevmaxsum)
            ## get global minimum sum so far
            resminsum = min(resminsum, prevminsum)
        ## return the maximum absolute global mimimum/ maximum
        return max(abs(resmaxsum),abs(resminsum))