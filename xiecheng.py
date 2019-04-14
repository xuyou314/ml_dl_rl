s=input()
nums=s.split(',')
nums=list(map(int,nums))
minindex1=0
d=[0]*5000
pred=[0]*5000
d[0]=nums[0]
for i in range(1,len(nums)):
    if(nums[i-1]<0):
        d[i]=nums[i]+d[i-1]
        pred[i]=pred[i-1]
    else:
        d[i]=nums[i]
        pred[i]=i
    if d[i]<d[minindex1]:
        minindex1=i
minindex2=0
if minindex1==0:
    minindex2+=1
d2=[0]*5000
d2[0]=nums[0]
for i in range(1,len(nums)):
    if i in range(pred[minindex1],minindex1+1):
        continue
    if nums[i-1]<0:
        d2[i]=nums[i]+d2[i-1]
    else:
        d2[i]=nums[i]
    if d2[i]< d2[minindex2]:
        minindex2=i
if minindex1 == len(nums)-1 and pred[minindex1] == 0:
    print(d[minindex1])
else:
    print(d[minindex1]+d[minindex2])