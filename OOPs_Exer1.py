class Reactangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    #creatting perimeter method
    def perimeter(self):
        return 2*(self.length+self.width)

    #creating area method
    def Area(self):
        return self.length*self.width

    #creating display method
    def display(self):
        print("The length is :",self.length)
        print("The width is :",self.width)
        print("The perimeter is :",self.perimeter())
        print("The Area is :",self.Area())

class parallelepipe(Reactangle):
    def __init__(self,length,width,height):
        Reactangle.__init__(self,length,width)
        self.height=height

    #creating volume method
    def volume(self):
        return self.length*self.width*self.height

react=Reactangle(5,9)  #react name object
react.display()

print("----------------------")
parr=parallelepipe(5,9,3)
print("The volume of parallelepipe is :",parr.volume())
