class Solution:
    ## function which returns the frequency of the smallest character
    def freq(self, s):
        smallest = s[0]
        count = 1
        ## find the smallest character and count the no of occurrence
        for i in s[1:]:
            if smallest > i:
                smallest = i
                count = 1
            elif smallest == i:
                count+=1
        return count
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        ## counter function to create a  dictionary with key(frequency of smallest character) ad value(no of such words)
        d = Counter([self.freq(i) for i in words])
        print(d)
        
        ## for every query, count no of words which has freq less than the words
        for i in range(len(queries)):
            q = self.freq(queries[i])
            c = 0
            for j in d:
                if q < j:
                    c += d[j]
            queries[i] = c 
        return queries