#!/usr/bin/python

def is_prime (n) :
   m = int(n**0.5)
   for i in range (2,m+1) :
      if (n%i == 0) :
         return 0

   return 1

sum = 0;

for i in range (2,10) :
	if is_prime (i) :
		sum+=i

print sum
