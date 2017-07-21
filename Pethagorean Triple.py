def main():
	N = eval(input("N = ?"))
	if N>0:
		for a in range(1,N-1):
			for b in range(a+1,N):
				for c in range(b+1,N+1):
					if a*a+b*b == c*c:
						print(a,"*",a,"+",b,"*",b,"=",c,"*",c)
main()
