n = int(input())

sum_val=0

if n <= 100:
    for i in range (n, 101):
        sum_val += i
    print(sum_val)