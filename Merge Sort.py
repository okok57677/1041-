import random
def merge(list1,list2,lists):
	i, j, k =0, 0, 0
	while i < len(list1) and j < len(list2):
		if list1[i] < list2[j]:
			lists[k]=list1[i]
			i=i+1
		else:
			lists[k]=list2[j]
			j=j+1
		k=k+1

	while i < len(list1):
		lists[k]=list1[i]
		i=i+1
		k=k+1

	while j < len(list2):
		lists[k]=list2[j]
		j=j+1
		k=k+1
	for a in range(len(lists)):
		print(lists[a],end=" ")
	print()

def mergeSort(nums):
	n = len(nums)
	if n > 1:
		m = n//2
		nums1,nums2 = nums[:m],nums[m:]
		mergeSort(nums1)
		mergeSort(nums2)
		merge(nums1,nums2,nums)

def main():
	nl = []
	import random
	for i in range(8):
		r = random.randrange(0,100)
		nl.append(r)
	mergeSort(nl)

main()
