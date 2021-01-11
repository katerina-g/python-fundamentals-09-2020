command = input()

courses = {}

while not command == "end":
    course_name, student = command.split(" : ")

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student)

    command = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")

    for student in sorted(value):
        print(f"-- {student}")