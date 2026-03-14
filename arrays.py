##1.Find the Maximum Element in an Array
##Given an array, return the maximum value.
##arr=[1,2,3,4,5]
##k=min(arr)
##print(k)
##2.Sum of All Elements in an Array
##Write a function to calculate the sum of all elements in an array.
##arr=[1,2,3,4,5]
##k=sum(arr)
##print(k)
#3.Check if an Array is Sorted
##Return true if the array is sorted in ascending order.
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 3, 2, 4, 5]

print(is_sorted(arr1))  # Output: True
print(is_sorted(arr2))  # Output: False

