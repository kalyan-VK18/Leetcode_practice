nums=[1,2,3,4,50,78,99]
largest=0
second_largest=0
for num in nums:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print(second_largest)
