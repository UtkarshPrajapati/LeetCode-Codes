class Solution:
    def reorganizeString(self,s):
        ch_cnt,n=Counter(s),len(s)
        if max(ch_cnt.values())>(n+1)//2: return ""
        ans,i=['']*n,0
        for ch,cnt in ch_cnt.most_common():
            for _ in range(cnt):
                ans[i]=ch
                i+=2
                if i>=n: i=1
        return ''.join(ans)