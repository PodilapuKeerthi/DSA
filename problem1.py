#largest element in an array

n=int(input())#size of an array
arr=list(map(int,input().split()))#user input array

#appoarch 1(using "sorted")
#Time Complexity: O(n log n) - BAD APPROACH
sorted_arr=sorted(arr) #sorts in ascending order
print(sorted_arr[-1])   #prints last element from sorted array which is the largest element

#approach 2(using "max" built in function)
#Time Complexity: O(n)
print(max(arr))

#approach 3 (using loop)
#Time Complexity: O(n)
large_ele=arr[0]
for i in range(1,n):
    if arr[i]>large_ele:
        large_ele=arr[i]
print(large_ele)