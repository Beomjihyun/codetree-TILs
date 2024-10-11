arr_a = input().split()
arr_b = input().split()

a_m = int(arr_a[0])
a_e = int(arr_a[1])

b_m = int(arr_b[0])
b_e = int(arr_b[1])

if a_m > b_m:
    print("A")
elif a_m == b_m and a_e > b_e:
    print("A")
else:
    print("B")