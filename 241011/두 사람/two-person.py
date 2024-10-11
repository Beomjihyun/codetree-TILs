arr1 = input().split()
arr2 = input().split()

a1 , g1 = int(arr1[0]), arr1[1]
a2 , g2 = int(arr2[0]), arr2[1]

if (a1 >= 19 and g1 == 'M') or (a2 >=19 and g2 == 'M'):
    print("1")
else:
    print("0")