"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Ractangle:

    def __init__(self,length,width):
        self.__length =length
        self.__width = width

        def getarea():
            area = self.__length * self.__width
            return f"Area = {area}"
            def getParimeter(self):
                perimeter = (self.__length + self.__width) * 2
                return f"Perimeter = {perimeter}"
            def isSquare(self):
                if self.__length == self.__width:
                    return True
                else :
                    return False
                
myRactangle = Ractangle(10 , 2)
print(myRactangle.getarea())
myRactangle.getParimeter()
print (myRactangle.isSquare())
                                
    