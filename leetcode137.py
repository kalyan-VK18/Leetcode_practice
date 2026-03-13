from collections import defaultdict
nums=list(map(int,input().split()))
count=defaultdict(int)
for i in nums:
    count[i]+=1
for i,freq in count.items():
    if freq==1:
        print(i)
        break
else:
    print(-1)
