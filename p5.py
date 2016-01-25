#!/usr/bin/python

n = 1
while True :
	print n
	flag = 1
	for i in range (2,21) :
		if (n % i) != 0 :
			flag = 0
			break
	if flag :
		break
	n+=1

print n
