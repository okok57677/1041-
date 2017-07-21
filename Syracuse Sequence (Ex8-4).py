def main():
	a = eval(input("Input a natural number -- "))
	print(a,end=" ")
	while a != 1:
		if a%2 == 0:
			a = a/2
			
		else:
			a = 3*a + 1

		print(int(a),end=" ")
	print()

if __name__ == "__main__":
	main()
