class MyPoint:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self):
        sum=(self.x)**2+(self.y)**2
        D=(sum)**(1/2)
        return D
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

def readPoints(name):
    infile=open( name,'r' )
    pointlist=infile.read().split("\n")
    listC=[]
    for i in range( len(pointlist)-1 ):
        xy=( pointlist[i] ).split()
        x,y=int( xy[0] ),int( xy[1] )
        listC = listC + [ MyPoint(x,y) ]
    return listC

def main():
    filename = input("Enter the name of the data file: ")
    myPoints = readPoints(filename)
    for i in myPoints:
        print( i, i.distance() )
main()
