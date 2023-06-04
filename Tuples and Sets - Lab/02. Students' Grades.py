count = int(input())
students = {}

for index in range(count):
    line = tuple(input().split())
    student, grade = line
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grade in students.items():
    grades_list = " ".join(str(f'{grad:.2f}') for grad in grade)
    average_grade = sum(grade) / len(grade)
    print(f"{student} -> {grades_list} (avg: {average_grade:.2f})")