with open("user.out","w") as f:
    for i in stdin: print((s:=i.rstrip())[:-1],",",s[1:],sep="",file=f)
    exit()