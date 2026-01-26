def fact(n):
    if n == 0:
        return 1
    val = fact(n-1)
    return n * val

print(fact(5))