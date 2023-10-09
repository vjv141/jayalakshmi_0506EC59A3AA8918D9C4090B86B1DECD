class student:
    def __init__(self,name,roll_number,cgpa):
        self.name=name
        self.roll_number=roll_number
        self.cgpa=cgpa
def sort_students(student_List):
    sorted_students=sorted(student_List,key=lambda student:student.cgpa,reverse=True) 
    return sorted_students
students=[
    student("Hari","A123",7.8),
    student("Baskaran","A124",8.9),
    student("Dharshini","A125",9.1),
    student("Ezhilarasan","A126",9.9)
] 
sorted_students=sort_students(students) 
for student in sorted_students:
    print("Name:{},Roll Number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))
