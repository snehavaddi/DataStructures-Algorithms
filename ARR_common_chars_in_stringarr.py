A = ["bella","label","roller"]
#chars = [c for i, c in enumerate(A[0]) if c not in A[0][:i]]
chars = []
for i,c in enumerate(A[0]):
        if c not in A[0][:i]:
                chars.append(c)
print(chars)


result = []
for c in chars:
    count = A[0].count(c)
    for w in A:
        if w.count(c) < count:
            count = w.count(c)
    for n in range(0, count):
        result.append(c)

print(result)