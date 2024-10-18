arr = input().split()

a = int(arr[0])
b = int(arr[1])

print("0.", end = "")

for _ in range(20):
    n = (a*10)//b
    a = (a*10) % b

    print(n, end = "")