def is_pal(s):
    n = len(s)
    if n == 0 or n == 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_pal(s[1:-1])


print(is_pal("Thaj"))
print(is_pal("ThajahT"))