def linear_search(lst, target):
 for i in range(len(lst)):
    if lst[i] == target:
     return i
 return -1
lst = [10, 20, 30, 40, 50]
target = 30

result = linear_search(lst, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")