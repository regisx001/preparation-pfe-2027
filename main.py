s = "Python is very powerful"

s_reversed = []

for i in range(len(s.split(" "))-1, -1, -1):
    s_reversed.append(s[i])


print(s_reversed)
