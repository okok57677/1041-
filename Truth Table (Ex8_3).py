def pq(x):
	if x == True:
		return "T"
	else:
		return "F"

def main():
	print("P\tQ\tnot(P or Q)\tnot p and not Q")
	print("===\t===\t===\t\t===")
	for P in [True,False]:
		for Q in [True,False]:
			a,b,c,d = P,Q,not(P or Q),not P and not Q		
			print(pq(a),pq(b),pq(c),'',pq(d),sep="\t")
if __name__ == "__main__":
	main()
