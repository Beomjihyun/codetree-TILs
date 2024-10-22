arr = input().split()

a, b = int(arr[0]), int(arr[1])

if a <= 0:
    print(0)

else:
    for i in range(b):
        print(a, end="")