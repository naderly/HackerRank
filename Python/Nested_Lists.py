python_students = list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    python_students.append([name, score])
    python_students.sort(key=lambda x: x[0])
    python_students.sort(key=lambda x: x[1])
for i in range(1, len(python_students)):
    if python_students[i][1] > python_students[i-1][1]:
        value = python_students[i][1]
        break
for i in range(len(python_students)):
    if python_students[i][1] == value:
        print(python_students[i][0])
# print(python_students)
# print(value)
