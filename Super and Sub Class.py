
class Student: #student class super class
    def __init__(self,name,college,major):
        self.name=name
        self.college=college
        self.major=major
        
    def __str__(self): #str method
        return f'Student({self.name},{self.college},{self.major})'
    
    def Print1(self): #print method
        print(self.name,'is a/an',self.major,'student at',self.college)
        

class GraduateStudent(Student): #graduatestudent class sub class
    def __init__(self,name,college,major,project,scholarship):
        self.project = project
        self.scholarship = scholarship
        Student.__init__(self,name,college,major)
        
    def __str__(self): #str method
        return f'GraduateStudent({self.project},{self.scholarship})'
    
    def Print2(self): #print method
        print(self.name,'is a/an',self.major,'graduate student at',self.college,', working on project',self.project,
              ', receiving',self.scholarship,'as scholarship.')
        
    

def main(): #main method
    #inputs as instances
    s1=Student('Steve','NEC','English')
    s1.Print1()
    s2=GraduateStudent('Mary','Harvard','CS','AI','$3500')
    s2.Print2()
    
    #s1=Student('Alicia','MIT','Mechanical Engineering')
    #s1.Print1()
    #s2=GraduateStudent('John','Yale','Pscholory','Dream Analysis','$7800')
    #s2.Print2()
       
if __name__ == "__main__":
  main()
