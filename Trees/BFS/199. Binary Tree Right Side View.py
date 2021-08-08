# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ## if empty tree
        if root==None:
            return []
        ## queue for storing nodes
        queue = collections.deque([root])
        ## final result list
        res = []
        ## until queue is empty
        while(queue):
            ## store node values at a level
            level = []
            for _ in range(len(queue)):
                ## pop left most node
                node = queue.popleft()
                ## add to level list
                level.append(node.val)
                ## add RIGHT and then LEFT child of parent to the queue
                if node.right!= None:
                    queue.extend([node.right])
                if node.left!=None:
                    queue.extend([node.left])
            ## add rightmost level item to the final result
            res.append(level[0])
        return res
                
            
        