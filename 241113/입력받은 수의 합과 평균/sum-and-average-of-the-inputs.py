n = int(input())

sum_val=0

for _ in range (n):
    i = int(input())
    sum_val += i
avg =sum_val/n

print(sum_val, f"{avg:.1f}")