class OrderedStream:
    def __init__(s,n):
        s.l,s.t=[None]*n,0
    def insert(s,idKey,value):
        s.l[idKey-1]=value
        res=[]
        for i in range(s.t,len(s.l)):
            if s.l[i]: res.append(s.l[i]);s.t+=1
            else: break
        return res