# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## if empty tree
        if root == None:
            return []
        ## final result list 
        res = []
        ## queue for storing nodes
        queue = collections.deque([root])
        ## until queue is empty
        while(queue):
            ## store node values at a level
            level = []
            for _ in range(len(queue)):
                ## pop left most node
                node = queue.popleft()
                ## add to level list
                level.append(node.val)
                ## add left and  right child of parent to the  queue
                if node.left  != None:
                    queue.extend([node.left])
                if node.right  != None:
                    queue.extend([node.right])
            ## add level list to the final result
            res.append(level)
        return res
                
            
        
        