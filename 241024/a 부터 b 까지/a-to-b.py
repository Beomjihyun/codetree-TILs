arr = input().split()

a = int(arr[0])
b = int(arr[1])
print(a, end=" ")

for _ in range(a,b+1):
    if a % 2 == 1:
        a *= 2

    elif a % 2 == 0:
        a += 3

    if a <= b:
        print(a, end=" ")