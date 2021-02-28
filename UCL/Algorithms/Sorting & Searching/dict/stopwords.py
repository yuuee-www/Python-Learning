stopwordsdict = dict()
with open('stopwords.txt','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        stopwordsdict[lines[i].rstrip('\n')] = 0
print("number of stopwords:", len(stopwordsdict)+1)

totalremoved = 0
removedstopwordsdict = dict()
punctuation = '''!()=[]{};:\,<>./?@#$%^&*_-~'''

with open('mobydick.txt','r') as f:
    lines = f.readlines()

    for i in range(len(lines)):
        lines[i].rstrip('\n')
        for c in lines[i]:
            if c in punctuation:
                lines[i] = lines[i].replace(c, "")
        for word in lines[i].split():
            key = word.lower()
            if stopwordsdict.get(key) is not None:
                if removedstopwordsdict.get(key) is None:
                    removedstopwordsdict[key] = 1
                else:
                    removedstopwordsdict[key] = removedstopwordsdict.get(key) + 1
                totalremoved += 1
print("number of stopwords removed:", totalremoved)

print(sorted(removedstopwordsdict.items(), key = lambda kv:kv[1], reverse = True))