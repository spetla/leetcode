"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ## if empty tree
        if root == None:
            return []
        
        ## create a queue to store the nodes
        queue = collections.deque([root])
        res = []
        
        ## iterate until queue is empty
        while queue:
            ## list to store node values at same level
            level = []
            ## iterate over all nodes present in the queue
            for i in range(len(queue)):
                ## pop left node
                node = queue.popleft()
                ## add node value to level list
                level.append(node.val)
                ## add children nodes to queue
                queue.extend(node.children)
            ## append level list to the global result list
            res.append(level)
        return res