s=input()
l=s[1:-1].split(',')
nums=list(map(int,l))
d=input()
d=int(d)
total=len(l)*(len(l)-1)/2
ct=0
for i in range(len(l)):
    for j in range(i,len(l)):
        if nums[i]-nums[j]>d or nums[i]-nums[j]<-d:
            ct+=1
print("%.6f"%(1-ct/total))