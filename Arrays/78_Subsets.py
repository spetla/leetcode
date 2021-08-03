class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## output list with default empty list
        res = [[]]
        ## iterate over all numbers
        for i in nums:
            ## append current element i to all the existig lists in the result list
            ## and add those new lists to the existing result list of lists 
            res += [j+[i] for j in res]
        return res