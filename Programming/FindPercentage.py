n = int(input())
student_marks = {}
for i in range(n):
    name, *score = input().split()
    score = list(map(float, score))
    student_marks[name] = score
target_name = input()
for name, score in student_marks.items():
    if name == target_name:
        avg = sum(score)/len(score)
print(f"{avg:.2f}")