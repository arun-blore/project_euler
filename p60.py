#!/usr/bin/python

# Create a list of prime numbers between 1 and N
primes = []

N = 10000

# check if a number is prime:
# say we want to check if n is prime
# if it is not prime, it must have a prime factor between 2 and sqrt(n)
# 
# a better method is to use the sieve of erastothenes

is_prime = [True] * N
is_prime [0] = False
is_prime [1] = False

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
for p in primes :
	graph_primes [p] = set([])

i = 0
for p1 in primes :
	for p2 in primes[i+1:] :
		#print i, j
		num1 = int(str(p1)+str(p2))
		num2 = int(str(p2)+str(p1))
		if (num1 > N) or (num2 > N) :
			break
		else :
			if is_prime[num1] and is_prime[num2]:
				print p1, p2, num1, num2
				graph_primes[p1].add(p2)
				graph_primes[p2].add(p1)
	i+=1


gp = {}
for p in graph_primes :
	if (len(graph_primes[p]) != 0) :
		gp[p] = graph_primes[p]

# print gp


def find_cliques (k) :
	"""
	This function takes an input undirected graph and an integer k (>= 3). graph is a dictionary.
	It returns a list of cliques of size k.
	Each clique is a list of nodes
	"""
	## cliques = []
	## # any node with degree lower than k-1 cannot be a node in a clique of n nodes
	## # remove any nodes with degree lower than k-1 from graph
	## graph_pruned = {}
	## for node in graph :
	## 	if (len(graph[node]) >= k-1) :
	## 		graph_pruned[node] = graph[node]

	## # for every combinaton of k nodes in graph_pruned, check if the nodes form a clique
	## all_nodes = graph_primes.keys ()
	## n = len(all_nodes)

	n = 6
	num_cliques = 0

	comb = range (0, k)
	end_comb = range (n-k, n)
	while True :
		# check if nodes pointed to by indices in comb form a clique
		print comb
		num_cliques+=1

		if comb == end_comb :
			print num_cliques
			break

		# create the next combination
		ind = k-1
		while True :
			if comb[ind] == end_comb[ind] :
				ind-=1
			else :
				comb[ind]+=1
				for ind1 in range (ind+1, k) :
					comb[ind1] = comb[ind] + ind1-ind
				break

find_cliques (3)
