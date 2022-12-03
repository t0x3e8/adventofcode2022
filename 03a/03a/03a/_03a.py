
import numpy as np

fContent =  open("input.txt", "r").readlines();

def split(line):
    n = len(line)
    return line[:(n//2)], line[(n//2):]

def intersection(s1, s2):
    for i in s1:
	    if i in s2:
		    return i

sum = 0
for line in fContent:
    s1, s2 = split(line.strip())
    l = intersection(s1, s2)
    diff = 38 if l.isupper() else 96
    sum += ord(l) - diff

    print(sum)

print(sum)
