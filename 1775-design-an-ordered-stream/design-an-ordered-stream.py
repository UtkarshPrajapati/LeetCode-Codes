class OrderedStream:
    def __init__(self,n):
        self.t,self.l=1,[None]*(n+2)
    def insert(self,idKey,value):
        self.l[idKey]=value
        if idKey==self.t:
            while self.l[self.t]: self.t+=1
            return self.l[idKey:self.t]