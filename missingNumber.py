n = int(input("hi:"))
l = list()
for i in range(1,n):
    l = l + [int(input())]

j = 0
n = len(l)
while j < n-1:
    if l[j] != j+1:
        print(j+1)
        break
    j = j + 1
