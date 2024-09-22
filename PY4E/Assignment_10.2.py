name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        timestamp=line.split()[5]
        hours=timestamp[:2]
        counts[hours]= counts.get(hours, 0) + 1
newsorted = sorted([(h,c) for h,c in counts.items() ], )

for h,c in newsorted:
    print(h, c)


