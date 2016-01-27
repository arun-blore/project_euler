#!/usr/bin/python

n = 600851475143
max = int(n**0.5)

def is_prime (n) :
   m = int(n**0.5)
   for i in range (2,m+1) :
      if (n%i == 0) :
         return 0

   return 1

#print is_prime(3), is_prime(10), is_prime(23), is_prime(100)

for i in range (max, 2, -1) :
   if (n%i == 0) :
      if (is_prime(i)) :
         print i
         break
