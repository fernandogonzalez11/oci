n = int(input())
plantas = [int(x) for x in input().split()]

costo = 0

indexes = {}
for i in range(n):
    indexes[plantas[i]] = i

for i in range(1, n):
    costo += i * abs(indexes[i] - indexes[i+1])

print(costo)