def anagrams(alist):
    dic = {}
    for i in alist:
        k = ''.join(sorted(i))
        if k not in dic:
            dic[k] = []
        dic[k].append(i)
    return [dic[j] for j in dic]


alist =  ['eat', 'tea', 'part', 'ate', 'trap', 'pass']
print(anagrams(alist))