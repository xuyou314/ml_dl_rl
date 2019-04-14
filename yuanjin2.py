s=input()
s=s.replace('[','')
s=s.replace(']','')
nums=s.split(',')
nums=list(map(int,nums))
ct=0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)-1):
        if nums[i]>nums[j]:
            ct+=1
print(ct)