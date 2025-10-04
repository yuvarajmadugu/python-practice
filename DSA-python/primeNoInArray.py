# arr=[]
# for i in range(0,11):
#     if i%2==0:
#         arr.append(i)
# print(arr)

arr = []

for i in range(2, 11):  # Prime numbers start from 2
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):  # Check divisibility up to √i
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        arr.append(i)

print(arr)
