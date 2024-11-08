arr = list(range(1,12216))
target = 1781

left = 0
right = len(arr) - 1
found = False

while left <= right and not found:
    mid = (left + right) // 2
    
    if arr[mid] == target:
        found = True
    elif target < arr[mid]:
        right = mid - 1
    else:
        left = mid + 1

if found:
    print("Target found at index", mid)
else:
    print("Target not found")
