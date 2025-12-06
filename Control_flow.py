student_data = {'marks':[10, 20, 30, 40]}
att=75
for keys, values in student_data.items():
    total_marks = sum(values.items())
    print(total_marks)
    if total_marks > 75 and att >= 75:
        print("Excellent")
    else:
        print("need to improve performance")
