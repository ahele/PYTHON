import re
handle=open("regex_sum_42.txt")
content = handle.read()
val =re.findall('[0-9]+', content)
valnew=[]
for x in val:
    x=int(x)
    valnew.append(x)
print(sum(valnew))