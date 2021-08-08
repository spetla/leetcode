"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return None
        
        queue = collections.deque([root])
        
        while(queue):
            l = len(queue)-1
            for i in range(len(queue)):
                node = queue.popleft()
                if l == i:
                    node.next = None
                else:
                    node.next = queue[0]
                
                if node.left!=None:
                    queue.extend([node.left])
                if node.right!=None:
                    queue.extend([node.right])
                    
        return  root