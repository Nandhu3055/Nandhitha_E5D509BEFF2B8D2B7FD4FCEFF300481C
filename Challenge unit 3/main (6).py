class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


students = [
    Student("Ananya", "123", 3.75),
    Student("Bhavani", "456", 3.89),
    Student("Catherine", "789", 3.65),
    Student("Dharshana", "101", 3.95),
]

sorted_students = sort_students(students)

for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number},CGPA: {student.cgpa}")
