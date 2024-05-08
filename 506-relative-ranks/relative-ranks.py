class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ss=sorted(score,reverse=True)
        for i,n in enumerate(score):
            ind=ss.index(n)
            if ind==0: score[i]="Gold Medal"
            elif ind==1: score[i]="Silver Medal"
            elif ind==2: score[i]="Bronze Medal"
            else: score[i]=str(ind+1)
        return score