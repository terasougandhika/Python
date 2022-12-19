

#class Shape
class Shape:
    ##init method
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    ##str method
    def __str__(self):
        return  f' Shape({self.color},{self.filled})'

#Triangle another method
class Triangle(Shape):
    ##init method
    def __init__(self,s1,s2,s3,color,filled):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        super().__init__(color,filled)
        

    #str method
    def __str__(self):
        return  f'Triangle({self.s1},{self.s2},{self.s3},{self.color},{self.filled})'

    #area method
    def area(self):
        s=(self.s1+self.s2+self.s3)/2
        area_x=(s*(s-self.s1)*(s-self.s2)*(s-self.s3)) ** 0.5
        return area_x

    #perimeter method
    def perimeter(self):
        perimeter_x=self.s1+self.s2+self.s3
        return perimeter_x

def output(s1,s2,s3,t_area,t_perimeter,color,filled):
    print("A triangle 3 sides are: ({} ,{} ,{})".format(s1,s2,s3))
    print("Triangle Area is :",t_area)
    print("Triangle Perimeter is: ",t_perimeter)
    print("Color of the Triangle is :",color)
    if(filled):
        print("Triangle is filled with color")
    else:
        print("Triangle is not filled with color")
        
          

#main function
def main():
    while True:
        try:
            s1=float(input("Enter side1: "))
            s2=float(input("Enter side2: "))
            s3=float(input("Enter side3: "))
            #check triangle property
            if(s1>s2+s3 or s2>s1+s3 or s3>s1+s2 or s1<abs(s2-s3) or s2<abs(s1-s3) or s3<abs(s1-s2)):
                print("The input cannot form a triangle!")
                continue
            break
        except:
            print("Input integer or floating-point for sides")
            
    color=input("Enter color: ")
    filled=bool(input("Enter  1/0 for filled (1: True, 0:False): "))
    
    t=Triangle(s1,s2,s3,color,filled)
    t_area=t.area()
    t_perimeter=t.perimeter()
    output(s1,s2,s3,t_area,t_perimeter,color,filled)
    
    

#main proccess
if __name__=="__main__":
    main()

