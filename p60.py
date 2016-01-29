#!/usr/bin/python

# Create a list of prime numbers between 1 and N
primes = []

N = 2000000

# check if a number is prime:
# say we want to check if n is prime
# if it is not prime, it must have a prime factor between 2 and sqrt(n)
# 
# a better method is to use the sieve of erastothenes

is_prime = [True] * N

i = 2
done = 0
sum = 0

while True:
	#print i
	primes.append(i)
	ind = i*i
	sum+=i
	while ind < N :
		is_prime [ind] = False
		ind+=i
	# find the next prime
	i+=1
	if i >= N :
		break

	while not is_prime[i] :
		i+=1
		if i >= N :
			done = 1
			break

	if done :
		break

print len(primes)

# construct a graph with each node being a prime number and adjacent nodes have the property where
# these primes can be concatenated in any order to produce another prime
graph_primes  = {}

for i in range (len(primes)) :
	for j in range (i+1, len(primes)) :
		#print i, j
		num = int(str(primes[i])+str(primes[j]))
