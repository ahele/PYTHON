# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
collect=[]
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line.find("0")
    fnum=float(line[x:])
    collect.append(fnum)
num = 0.00
for i in collect:
    num=num+i
denom=float(len(collect))
print("Done")
print("Average spam confidence:", num/denom)