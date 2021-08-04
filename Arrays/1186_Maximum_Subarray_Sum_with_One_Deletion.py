class Solution:
	## Kadane's algorithm
    ## [1,-3,2,3,-4]
    ##  
    ##           -4
    ##         3
    ##       2,5, 1 ==> max = 5
    ##    -3
    ##  1,-2,0
    def maximumSum(self, arr: List[int]) -> int:
    	## variable which stores the local maximum sum with out deletion
    	prevmaxsum = -float(inf)
    	## variable which stores the local maximum sum with deletion 
    	prevmaxsumwithdel = -float(inf)
    	## variable which stores the overall global maximum sum so far
    	res = -float(inf)

    	for ele in arr:
    		## either consider previous max sum with deletion already done 
    		## (or) only previous max sum without considerig the current element (i.e deleting current element)
    		prevmaxsumwithdel = max(prevmaxsumwithdel+ele, prevmaxsum)
    		## either cosider previous max sum + current element (or) current element only
    		prevmaxsum = max(prevmaxsum+ele, ele)
    		## find max between current global max sum , prevmaxsumwithdel annd premaxsum
    		res = max(res,prevmaxsumwithdel,prevmaxsum)
    	return res
