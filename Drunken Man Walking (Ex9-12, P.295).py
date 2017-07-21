from random import random

def main():
	p = getInput()
	n = simOnelteration(p)
	printsummary(n)

def getInput():
	p = eval(input("Input the initial position(p) -- "))
	return p

def simOnelteration(P):
	while P > 1  and P < 10:
		LR = random()
		if LR <.5:
			print("|"+" "*(P-1)+"*"+" "*(9-P)+"|")
			P = P+1
		else:
			print("|"+" "*(P-1)+"*"+" "*(9-P)+"|")
			P = P-1
	return P

def printsummary(p):
	if p == 0:
		print("He arrives home safely.")
	elif p == 10:
		print("He falls into a river in a cold winter!")

if __name__ == "__main__":
	main()
