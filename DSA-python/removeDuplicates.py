arr = [1,1,2,3,4,4,5,7]
#remove duplicates in an array
res = []
for i in arr:
    if i not in res:
        res.append(i)
print(res)

