c = 65
n = 7
t = n // 2 +1
for i in range(1, t+1):
    print(" "*(t-i), end = "")
    for j in range(i):
        print(chr(c+i-j-1), end="")
    for k in range(i-1):
        print(chr(c+k+1), end="")
    print()

for l in range(t-1, 0, -1):
    print(" "*(t-l), end="")
    for p in range(l):
        print(chr(c+p), end="")
    for q in range(l-1):
        print(chr(c+l-2-q), end="")
    print()