fname = input("Enter the name of the file:")
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)
counts = dict()

for line in fhand:
    sline = line.rstrip()
    if sline.startswith('From '):
        dspace_pos = sline.find('  ')
        tpos = sline.find(':', dspace_pos)
        hpos = sline[dspace_pos+3 : tpos]
        #print(hpos)
        hpos = hpos.lstrip()
        counts[hpos] = counts.get(hpos, 0) + 1
        #print(counts)

lst = list()
for k,v in counts.items():
    new_tup = (k,v)
    lst.append(new_tup)
lst = sorted(lst)
#print(lst)

for k,v in lst:
    print(k,v)