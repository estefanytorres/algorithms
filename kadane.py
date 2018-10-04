# Kadane's Algorithm is used to find the maximum subarray within an array
def kadane(arr):
    max_current = max_global = arr[0]
    from_global = to_global = from_current = to_current = 0
    for i in range(1,len(arr)):
        to_current = i
        if arr[i] > (max_current+arr[i]):
            from_current = i
            max_current = arr[i]
        else:
            max_current = max_current+arr[i]
        if max_current > max_global:
            from_global = from_current
            to_global = to_current
            max_global = max_current 
    return arr[from_global:to_global+1]
    
# Example array
ex = [1, -3, 5, -2, 9, -8, -6, 4]

# Result would be [5, -2, 9]
print(kadane(ex))
