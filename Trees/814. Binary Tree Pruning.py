# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## check if root node and it childrens has one or not
        if self.checkforone(root)==False:
            return None
        else:
            return root
    
    ## function to check if left or right nodes of a node have one or not
    def checkforone(self,node):
        ## if it is empty node return False
        if node == None:
            return False

        ## Traverse and check if left node has one or not
        left = self.checkforone(node.left)
        ## Traverse and check if right node has  one or not
        right = self.checkforone(node.right)

        ## if  left node doesnot have 1 remove it
        if left == False:
            node.left = None 

        ## if right node doesnot have 1 remove it
        if right == False:
            node.right = None 

        ## if a node value is zero and none of its childern has 1 then return False
        if node.val == 0 and right == False and left == False:
            return False
        else:
            return True