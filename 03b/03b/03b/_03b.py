fContent =  open("input.txt", "r").readlines();

def intersection(l1, l2, l3):
    for i in l1:
	    if i in l2 and i in l3:
		    return i

sum=0
for i in range(0, len(fContent), 3):
	l1, l2, l3 = fContent[i], fContent[i+1], fContent[i+2]
	l = intersection(l1, l2, l3)
	diff = 38 if l.isupper() else 96
	sum += ord(l) - diff

print(sum)