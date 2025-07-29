#Method 1 Linear search 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(f"The Number is at", linear_search([3, 7, 9, 1], 9), "place")

