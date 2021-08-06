class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ## global result set
        self.res = set()
        ##visited power tuple set
        self.visited = set()
        ## DFS fucntion
        self.DFS(x,y,0,0,bound)
        return list(self.res)
    
    def DFS(self,x,y,px,py,bound):
        ## check if power tuple already existing in the visited nodes list
        ## return to stop branching
        if (px,py) in self.visited:
            return
        
        ## compute the power sum
        val = x**px+y**py
        
        ## check if power sum is greater than bound
        ## return to stop branching
        if val > bound:
            return
        
        ## Add new power tuple to global visited nodes list
        self.visited.add((px,py))
        
        ## Add result to global result set
        self.res.add(val)
        
        ## if x is not 1 create left branch
        if x>1:
            self.DFS(x,y,px+1,py,bound)
            
        ## if y is not 1 create right branch
        if y>1:
            self.DFS(x,y,px,py+1,bound)
        
        return