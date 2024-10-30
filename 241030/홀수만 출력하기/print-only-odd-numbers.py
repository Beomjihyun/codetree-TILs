n=int(input())

arr = [0 for i in range(n)]

for i in range(0,n):
    arr[i] = int(input())

for i in range(0,n):
    if arr[i] % 2 == 1 and arr[i] % 3 == 0:
        print(arr[i])