name = input('Enter file name: ')
fhandle = open(name)

counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigword = None
bigcount = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print('Word is',bigword,'. and count is',bigcount)
