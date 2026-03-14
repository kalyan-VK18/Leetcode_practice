#1.median of two arrays
##nums1=list(map(int,input().split()))
##nums2=list(map(int,input().split()))
##arr=nums1+nums2
##arr.sort()
##n=len(arr)
##if(n%2==1):
##    print(float(arr[n//2]))
##else:
##    print(float((arr[(n-1)//2]+arr[n//2])/2))
#2.reverse the words and also remove extra space
##s=input()
##k=s.split()
##k.reverse()
##print(" ".join(k))
#3.integer to roman
##num=int(input())
##values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
##symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
##res=""
##for i in range(len(values)):
##    while num>=values[i]:
##        res+=symbols[i]
##        num-=values[i]
##print(res)
