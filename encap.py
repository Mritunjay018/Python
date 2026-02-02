class student:
    def __init__ (self,name,rollno,age):
        self.name = name #public ATTRIBUTE
        self._rollno = rollno # protected

        self.__age = age # 
        
        
    def __display(self):#private method
        print(f"hi myself {self.name}{self.__age} year old with rollno{self._rollno}")
    def displayprivate(self):
        self.__display()

class branch(student):
    def show(self):
        print(self._rollno)

s1 = student('jay',18,35)
#s1.displayprivate() # methood to display private data using class
s1._student__display()  # second methodusing name mangling


        
