fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
 #print(line.rstrip())
 w=line.split()
 for p in w:
        #print(p)

        lst.append(p)
#print(lst)
lst=list(set(lst))
lst.sort()
print(lst)
