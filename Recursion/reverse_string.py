def rev(s):
    if s == "":
        return s
    c = rev(s[1:])
    return c + s[0]

print(rev("Thaj"))