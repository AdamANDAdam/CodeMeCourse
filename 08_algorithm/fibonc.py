def sum_natural(n):
    sum_num = 0
    for i in range(1,n+1):
        sum_num += i

    return sum_num
def sum_nat_while(n):
    sum_num = 0
    while n > 0:
        sum_num += n
        n -= 1
    return sum_num
def sum_nat_recursion(n):
    if n == 1:
        return 1
    return n + sum_nat_recursion(n-1)
    # n + fun(n-1)

print(sum_natural(10))
print(sum_nat_while(10))
print(sum_nat_recursion(10))