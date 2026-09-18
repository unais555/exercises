class Student():
    def __init__(self, name, age, admission_no, mark):
        self.name = name
        self.age = age 
        self.admission_no = admission_no 
        self.mark = mark

    def displaly_result(self):
        if self.mark > 50:
            return(f"{self.name} : Pass")
        else:
            return(f"{self.name} : Fail")

    def calculate_grade(self):
        if self.mark >= 90 :
            grade = "A"
        elif self.mark >= 80:
            grade = "B"
        elif self.mark >= 70:
            grade = "c"
        elif self.mark >= 60:
            grade = "D"
        elif self.mark >= 50:
            grade = "E"
        elif self.mark < 50:
            grade = "F"
        return(grade)

student_1 = Student("John", 15, "12B34", 45)
student_2 = Student("Wicky", 16, "12B47", 68)

print(student_1.name)
print(student_2.admission_no)
print(student_1.displaly_result())
print(student_2.calculate_grade())