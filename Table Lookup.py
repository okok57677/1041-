def main():
	n = 1
	while n <= 100 and n > 0:
		n = eval(input("Input an integer between 1 and 100 -- "))
		if n == 0 or n >= 100: break
		prime(n)

def prime(n):
	primeL = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	if n in primeL: 
		print(n,"is a prime number with index",primeL.index(n))
	elif not(n in primeL):
		print(n,"is NOT a prime number.")

if __name__ == "__main__":main()
