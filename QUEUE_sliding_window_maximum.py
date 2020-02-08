import collections

q = collections.deque([8, 5, 10, 7, 9, 4, 15, 12, 90, 13])
n = len(q)
k = 4
d = []
final = []
for i in range(n):
    if len(d) == 0:
        d.append(q[i])
    else:
        if q[i] > d[0]:
            d.clear()
            d.append(q[i])
            if i > k - 1:
                final.append(d[0])
        else:
            d.append(q[i])
            if i > k - 1:
                final.append(d[0])
    if i == k-1:
        final.append(d[0])

for i in range(len(final)):
    print(final[i],end=" ")

