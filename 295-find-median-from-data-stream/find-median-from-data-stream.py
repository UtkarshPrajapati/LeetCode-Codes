class MedianFinder:
    def __init__(self):
        self.l,self.c=[],0
    def addNum(self,num):
        if not self.l: self.l.append(num)
        else:
            for i in range(len(self.l)):
                if num<self.l[i]: self.l.insert(i,num);break
            else: self.l.append(num)
        self.c+=1
    def findMedian(self):
        return self.l[self.c//2] if self.c%2 else sum(self.l[self.c//2-1:self.c//2+1])/2