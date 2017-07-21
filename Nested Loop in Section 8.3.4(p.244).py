import random
def main():
	a = eval(input("How many lines of data you want to generate:"))
	for i in range(a):
		Z = random.randint(1,10)
		for j in range(Z):
			X=random.randint(1,100)
			print(X,end='')
			if j<Z-1:
				print(",",end='')
			else:
				print('')
main()
