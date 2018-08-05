class code_table:
    
    def __init__(self, maxn, base_field=GF(2)):
        self.maxn = maxn
        self.upper_bounds = {}
        self.lower_bounds = {}
        self._construction = {}
        for n in range(1,maxn+1):
            for k in range(1,n+1):
                self.upper_bounds[(n,k)] = n
                self.lower_bounds[(n,k)] = 1
                self._construction[(n,k)] = ""
                
    def add(self,C,designed_distance=None):
        """
        Method for adding a code to the database.

        inputs:
        C: code to add
        designed_distance: a lower bound for the min distance of C. You have to add this argument to avoid computing it.
        """
        #add code C to the database
        n = C.length()
        k = C.dimension()
        if designed_distance==None:
            d = C.minimum_distance()
        else:
            d=designed_distance
        self._construction[(n,k)] = C.__repr__()
        self.update_lower_bound(n,k,d)
        
                
                
    def update_lower_bound(self, N, K, d):
        """
        Update with a new lowerbound at [N,K]. This method also takes into account possible code shortenings, lengthenings and truncations.
        """
        nn = N
        kk = K
        self.lower_bounds[(nn,kk)] = d
        
        # add shortenings of the new code
        for k in range(1,kk+1):
            for n in range(nn-kk+k,self.maxn+1): 
                if d > self.lower_bounds[(n,k)]:
                    self.lower_bounds[(n,k)] = d
                    
                    #recipe
                    self._construction[(n, k)] = 'Derived from \n' + self._construction[(N, K)]
        
        # derive truncated codes
        while d>1 and nn>kk:
            nn=nn-1
            d=d-1
            if d > self.lower_bounds[(nn,kk)]:
                #recipe
                s = self._construction[(N,K)]
                if s.find("Trun") == -1:
                    self._construction[(nn,kk)] = 'Truncation of\n' + self._construction[(N,K)]
                self.update_lower_bound(nn, kk, d)
                     
                
    # PlotkinSum update (u|u + v)
    def plotkin_update(self,n):
        """
        Adds Plotkin sums ((u|u+v)) of all elements in row n to the table, if applicable.
        """
        if 2*n > self.maxn:
            return -1
        for k1 in range(1,n+1):
            for k2 in range(1,n+1):
                d1 = self.lower_bounds[(n,k1)]
                d2 = self.lower_bounds[(n,k2)]
                d = min(2*d1,d2)
                #recipe
                self._construction[(2*n, k1+k2)] = '%s Plotkin sum of [%s,%s,%s] and [%s,%s,%s]'%(d,n,k1,d1,n,k2,d2)
                #   re1 = self._construction[(n,k1)]
                #   re2 = self._construction[(n,k2)]
                #   re = "\n[%s,%s,%s] construction:\n"%(n,k1,d1) + re1 + "\n[%s,%s,%s] construction:\n"%(n,k2,d2) + re2
                #   self._construction[(2*n, k1+k2)] = self._construction[(2*n, k1+k2)] + re
                self.update_lower_bound(2*n, k1+k2, d)
                
    # juxtaposition update
    def juxtapose_update(self,k):
        """
        Adds juxtapositions of all elements in colums k to the table, if applicable.
        """
        maxn = self.maxn
        for n1 in range(k,maxn+1):
            for n2 in range(k,maxn+1):
                if n1 + n2 > maxn:
                    continue
                d1 = self.lower_bounds[(n1,k)]
                d2 = self.lower_bounds[(n2,k)]
                d = d1 + d2
                if d > self.lower_bounds[(n1+n2,k)]:
                    self.update_lower_bound(n1+n2,k,d1+d2)
                    #recipe
                    self._construction[(n1+n2,k)] = '%s Juxtapose [%s,%s,%s] and [%s,%s,%s]'%(d,n1,k,d1,n2,k,d2)
                
                
