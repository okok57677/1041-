import random

def selSort(nums):
	n = len(nums)
	for bottom in range(n-1):
		mp = bottom
		for j in range(8):
			print(nums[j],end="\t")
		print("\n")
		for i in range(bottom+1,n):
			if nums[i] < nums[mp]:
				mp = i
		nums[bottom],nums[mp] = nums[mp] , nums[bottom]
	for j in range(8):
		print(nums[j],end="\t")
	print()

def main():
	nl = []
	for i in range(8):
		x = random.randrange(0,100)
		nl.append(x)
	selSort(nl)

main()
