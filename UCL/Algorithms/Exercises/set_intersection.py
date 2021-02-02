def set_intersection(a, b):
    intersection = [i for i in a if i in b] #O(nm)
    intersection = list(set(a).intersection(set(b)))
    intersection = list(set(a) & set(b))
    intersection = list(filter(lambda x:x in a, b))


    return intersection