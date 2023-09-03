class Solution:
    def rearrangeArray(self,A):
        pos,neg=[],[]
        for i in range(len(A)):
            if A[i]>0: pos.append(A[i])
            else: neg.append(A[i])
        for i in range(len(pos)): A[2*i]=pos[i]
        for i in range(len(neg)): A[2*i+1]=neg[i]
        return A