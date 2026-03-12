nums1=input()
nums2=input()
n1=0
for i in nums1:
    n1=n1*10+(ord(i)-48)
n2=0
for j in nums2:
    n2=n2*10+(ord(j)-48)
print(str(n1*n2))
