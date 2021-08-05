class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        counts = [0]*(len(nums)+1)
        N = 10**9 + 7
        res = 0
        
        ## logic to count the overlaps with out two nested for loops
        for r in requests:
            counts[r[0]]+=1
            counts[r[1]+1]-=1
        
        for i in range(len(counts)-1):
            counts[i+1] = counts[i] + counts[i+1] 
        
        ## sort the counts and sort the nums and 
        ## multiple highest frequencies in counts array with the highest numbers
        for c,v in zip(sorted(counts[:-1],reverse=True),sorted(nums,reverse=True)):
            if c == 0:
                break
            else:
                res +=(c*v)%N 
                
        return res%N