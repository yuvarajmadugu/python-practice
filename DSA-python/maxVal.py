arr = [1,2,3,4]
maxval = 0

for i in range(len(arr)):
    if arr[i]>maxval:
        maxval = arr[i]
print(f"maxval in the given array {maxval}")