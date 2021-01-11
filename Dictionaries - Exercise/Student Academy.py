n = int(input())

students = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

filtered_students = {}
for student, grades in students.items():
    avr_grade = sum(grades) / len(grades)
    if avr_grade >= 4.50:
        filtered_students[student] = avr_grade

for student, avr_grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{student} -> {avr_grade:.2f}")
