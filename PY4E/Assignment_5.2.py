largest = None
smallest = None
collect=[] #for values from input
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:   
        inum = int(num)
    except:
        print("Invalid input")
        continue
    collect.append(inum)
for x in collect:
    if smallest == None:
        smallest = x
    elif smallest > x:
        smallest = x
for x in collect:
    if largest == None:
        largest = x
    elif largest < x:
        largest = x
print("Maximum is", largest)
print("Minimum is", smallest)