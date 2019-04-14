s=input()
nums=s.split(',')
a=input()
b=input()
aindex,bindex=-1,-1
for i in range(len(nums)):
    if a==nums[i]:
        aindex=i
    if b==nums[i]:
        bindex=i
while(aindex!=bindex):
    if(aindex>bindex):
        aindex=int((aindex+1)/2)-1
    if(bindex>aindex):
        bindex=int((bindex+1)/2)-1
print(nums[aindex])