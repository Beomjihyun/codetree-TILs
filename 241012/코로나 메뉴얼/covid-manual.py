arr1 = input().split()
arr2 = input().split()
arr3 = input().split()

c1, t1 = arr1[0], int(arr1[1])
c2, t2 = arr2[0], int(arr2[1])
c3, t3 = arr3[0], int(arr3[1])

if c1 == 'Y' and t1 >= 37:
    if (c2 == 'Y' and t2 >= 37) or (c3 == 'Y' and t3 >= 37):
        print('E')
    else:
        print('N')
elif c2 == 'Y' and t2 >= 37:
    if c3 == 'Y' and t3 >= 37:
        print('E')
    else:
        print('N')
else:
    print('N')