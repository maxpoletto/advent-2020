#!/opt/local/bin/python

filename = "input01.txt"
target = 2020

n = []
with open(filename) as f:
    for l in f:
        n.append(int(l))
n.sort()
print(n)
i, j = 0, len(n)-1
while True:
    if i >= j:
        print("Not found")
        exit(1)
    s = n[i]+n[j]
    if s > target:
        j = j-1
    elif s < target:
        i = i+1
    else:
        print(n[i], "and", n[j], "add up to", target, "and their product is", n[i]*n[j])
        exit(0)
