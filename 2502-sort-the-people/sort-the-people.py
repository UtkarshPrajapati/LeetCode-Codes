class Solution:
    def sortPeople(self,nms,hts):
        return[n for _,n in sorted(zip(hts,nms),reverse=True)]