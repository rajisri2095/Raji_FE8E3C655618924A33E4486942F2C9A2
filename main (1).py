'''Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.'''

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Creating a list of student objects
students = [
    Student("Alice", "A001", 3.9),
    Student("Bob", "B002", 3.5),
    Student("Charlie", "C003", 3.7),
    Student("David", "D004", 3.8),
]

# Sorting the list of students by CGPA in descending order
sorted_students = sort_students(students)

# Printing the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
