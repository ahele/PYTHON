fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    cline=line.split()
    for word in cline:
        if word in lst:
            continue
        lst.append(word)
lst.sort()
print(lst)
