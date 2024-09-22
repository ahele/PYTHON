# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,"r")
fhread=fh.read()
fhstrip=fhread.strip()
fhcaps = fhstrip.upper()
print(fhcaps)