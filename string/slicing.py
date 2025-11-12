"""
#### SLICING ####
# Slicing is a concept of Substringwith the help of index
# Syntax string[start:end:step]
# start - The index where the slice begin (default = 0)
# end - The index where the slice stops (default = len(string))
# step - The jump size (default = 1)
"""

word ="Thajunniza"

print(word[1:5:2])
print(word[:5:2])
print(word[3::2])
print(word[6:10])
print("reverse:" + word[::-1])

