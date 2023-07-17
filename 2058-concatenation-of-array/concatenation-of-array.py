f=open("user.out","w")
for i in stdin: print(i.rstrip()[:-1],",",i.rstrip()[1:],sep="",file=f)
exit()