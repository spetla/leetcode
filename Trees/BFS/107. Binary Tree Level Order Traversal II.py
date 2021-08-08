# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if  root == None:
            return []
        
        queue = collections.deque([root])
        
        res =[]
        
        while(queue):
            level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.extend([node.left])
                if node.right:
                    queue.extend([node.right])
                
            res.append(level)
        return  res[::-1]
            
            
        