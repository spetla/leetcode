class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ## dictionary to store the running sun
        check = {0:-1}
        runningsum = 0
        res = 0
        for i in nums:
            ## calculate the current running sum
            runningsum += i
            ## check if difference of current running sum and target is present in the dictionary
            ## if presennt then there exists a subarray with a sum = target
            if runningsum - target in check:
                ## re-initialize the check dictionary
                check = {}
                res += 1
            ## add the current running sum to the  dictionary
            check[runningsum] = i
        return res