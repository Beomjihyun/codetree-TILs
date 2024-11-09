sum_val=0
cnt =0
for _ in range(10):
    n = int(input())
    if n>=0 and n<=200:
        cnt += 1
        sum_val += n
print(f"{sum_val}", end = " ")
print(f"{(sum_val/cnt):.1f}")