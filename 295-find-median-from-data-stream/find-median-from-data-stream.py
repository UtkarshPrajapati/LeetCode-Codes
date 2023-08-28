class MedianFinder:
    def __init__(self):
        self.l,self.c=[],0
    def addNum(self,num):
        if not self.l: self.l.append(num)
        else:
            x,y=0,len(self.l)-1
            while x<=y:
                m=(x+y)//2
                if self.l[m]==num: self.l.insert(m,num);break
                elif self.l[m]<num: x=m+1
                else: y=m-1
            else: self.l.insert(x, num)
        self.c+=1
    def findMedian(self):
        return self.l[self.c//2] if self.c%2 else sum(self.l[self.c//2-1:self.c//2+1])/2