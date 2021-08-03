class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ## stack for storing the indexes
        s = []
        ## result array with -1's to start
        res = [-1]*len(nums)
        ## iterate the nums list twice
        for j in range(2):
            ## Iterate in reverse order
            for i in range(len(nums)-1,-1,-1):
                ## if stack is empty continue
                if not s:
                    s.append(i)
                    continue
                ## if top of stack index element is less than or equal to current element
                ## pop all indexs until we find an index element which is > current element
                ## Add to result array and append the current index into the stack
                elif nums[s[-1]] <= nums[i]:
                    while s and nums[s[-1]] <= nums[i]:
                        s.pop()
                    if not s:
                        s.append(i)
                        continue
                    else:
                        res[i] = nums[s[-1]]
                        s.append(i)
                ## if top of stack index element is less than current element 
                ## Add to result array and append the current index into the stack
                else:
                    res[i] = nums[s[-1]]
                    s.append(i)
        return res
                