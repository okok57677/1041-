class Student:
	def __init__(self,name,weight,height):
		self.name = name
		self.w = float(weight)
		self.h = float(height)
	def bmi(self):
		return self.w/(self.h)**2
def main():
	aList = [ Student("Alice", 50, 1.5),Student("Bob", 70, 1.7),Student("Claire", 60, 1.65) ]
	for i in aList:
		print(i.name, i.bmi())
main()
