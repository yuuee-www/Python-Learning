def root(i):
    while i != id[i]:
        i = id[i]
    return i

def connected(u,v):
    return root(u) == root(v)

def union(u,v):
    r_u = root(u)
    r_v = root(v)
    if r_u == r_v: 
        return
    if size[r_u] < size[r_v]:
        id[r_u] = r_v
        size[r_v] += size[r_u]
    else: 
        id[r_v] = r_u
        size[r_u] += size[r_v]

def find(u):
    r = []
    for i in range(len(id)):
        r.append(root(i))
    #print(r)
    print(max([i for i in range(len(r)) if r[i] == r[u]]))

#init
id = []
size = []
for i in range(8):
    id.append(i)
    size.append(1)