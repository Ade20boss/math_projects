import math
def check_prime(start, stop):
	primes = 0
	for i in range(start, stop):
		if i == 1 or i == 0: 
			continue
		elif i % 2 == 0 and i > 2:
			continue
		count = 0
		for j in range(2,  round(math.sqrt(i))+1):
			if i % j==0:
				count += 1
				break
		if count > 0:
			print(f"{i} is not prime")
		else:
			print(f"{i} is prime")
			primes += 1
	print(f"There are {primes} in that range")


def check_mersenne_primes(start,  stop):
	index1 = []
	mersenee_primes = 0
	for i in range(start, stop):
		index1.append((2**i)-1)
	for j in index1:
		count = 0
		if j % 2 == 0:
			continue
		for k in range(2, round(math.sqrt(j))+ 1):
			if j % k == 0:
				count += 1
				break
		if count > 0:
			print(f"{j} is just a  mersenne number")
		else:
			print(f"{j} is a mersenne prime")
			mersenee_primes += 1
	print(f"There are {mersenee_primes} fermat primes in the range")


def check_fermat_primes(start,  stop):
	index1 = []
	fermat_primes = 0
	for i in range(start, stop):
		count = 0
		index1.append(2**(2**i)+1)
	for j in index1:
		if j % 2 == 0:
			continue
		for k in range(2, round(math.sqrt(j)) + 1):
			if j % k == 0:
				count += 1
				break
		if count > 0:
			print(f"{j} is just a  fermat number")
		else:
			print(f"{j} is  a fermat prime")
			fermat_primes += 1
	print(f"There are {fermat_primes} fermat primes in the range")


#check_prime(1, 1000)
#check_fermat_primes(1, 1000)
check_mersenne_primes(1, 50)

				




			
				




