arr = input().split()

a = int(arr[0])
b = int(arr[1])


for i in range(21):
    m = a // b
    n = a % b
    a = n * 10

    print(m, end = "")

    if i == 0:
        print(".", end="")