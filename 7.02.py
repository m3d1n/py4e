# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
s=0
count=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    line=line.rstrip()
    #print(line)
    count=count+1
    x=line.find("0")
    n=line[x:]
    n=float(n)
    #print(n)
    s=n+s


#print("Done")
print(s/count)
