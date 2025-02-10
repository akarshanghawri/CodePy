def binary_search(arr, query) :
    lo = 0
    hi = len(arr) - 1

    while lo <= hi :       
        mid = (lo + hi) // 2
        if arr[mid] == query :
            return mid 
        elif arr[mid] < query :
            lo = mid + 1            #searches right half
        else :
            hi = mid - 1            #searches left half

    return -1       #if not present returns -1
