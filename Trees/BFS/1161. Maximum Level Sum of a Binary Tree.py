# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        ## variable to store maximum sum 
        maxsum = -float(inf)
        ## level couter
        count = 1
        ## result level
        res = 1
        ## queue to store the nodes
        queue = collections.deque([root])
        
        ## until queue is empty
        while(queue):
            ## initiate level sum
            s = 0
            for _ in range(len(queue)):
                ## pop left most queue node
                node = queue.popleft()
                ## add it to the sum
                s = node.val + s
                ## add left and right nodes to queue
                if node.left != None:
                    queue.extend([node.left])
                if node.right != None:
                    queue.extend([node.right])
            ## check if current maxsum is less than level sum ad update accordingly 
            if maxsum < s:
                res = count
                maxsum = s
            ## increment level counter
            count += 1
        
        return res
            
        