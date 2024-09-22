name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
senders=[]
for line in handle:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        splt=line.split()[1]
        senders.append(splt)
for sender in senders:
    counts[sender]= counts.get(sender, 0) + 1
big_sender = None
sender_count = None
for sender,count in counts.items():
    if big_sender is None or count > sender_count:
        big_sender=sender
        sender_count=count
print(big_sender,sender_count)


