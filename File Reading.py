def main():
	fname = input("Please input a file name - ")
	infile = open(fname,"r")
	i = 1
	for line in infile.readlines():
		print(i,line[:-1])
		i = i+1
main()
