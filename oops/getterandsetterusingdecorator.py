class student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks= marks

    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,value):
        if 0<= value <= 100:
            self.__marks = value
        else:
            print("marks is between 0 to 100")

s = student("jay",21)
print(f"marks befor setter {s.marks}")
s.marks=33
print(f"marks after setter{s.marks}")
