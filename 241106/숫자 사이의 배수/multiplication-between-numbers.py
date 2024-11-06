arr = input().split()
a, b = int(arr[0]), int(arr[1])

sum_val = 0
count = 0

for i in range (a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        count += 1
        sum_val += i

print(sum_val, end = " ") 
print(f"{(sum_val/count):.1f}")