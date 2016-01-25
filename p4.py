#!/usr/bin/python

def palindrome (n) :
	s = str(n)
	for i in range(len(s)/2) :
		if s[i] != s[-(i+1)] :
			return 0
	return 1

# print palindrome (22)
# print palindrome (23)
# print palindrome (202)
# print palindrome (2002)


l = 0
for a in range (100,1000) :
	for b in range (100,1000) :
		prod = a*b
		if palindrome(prod) :
			if prod > l :
				l = prod

print l
