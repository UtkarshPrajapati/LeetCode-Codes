class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        k=[]
        [k.append(i) for i in key if i not in k and i!=" "]
        return "".join([chr(k.index(i)+97) if i!=" " else " " for i in message])
