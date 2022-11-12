
n = int(input('n '))
student_marks = {}
for _ in range(n):
    name, *line = input('nev ertek ertek ertek ').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input('query')
    
print(format(sum(student_marks[query_name]) / len(student_marks[query_name]),'.2f'))