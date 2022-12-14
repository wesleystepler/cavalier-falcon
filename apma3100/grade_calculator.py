w = [(18.5/20), (19/20), (20/20), (12/20), (16.75/20), (19.5/20), (15/20), (11/20), (10/20), (12.4/20), (6.25/20), (17.5/19), (8/20), (9.5/20), (17.5/20), (12.25/20), (9.5/20), (15/20), 0]
worksheets = sum(w)/len(w)
print(worksheets)
ws = 0.5
webwork = 0.7666
preclass = 0.95
project1 = 0.6
project2 = 0.88
project3 = 0.6
exam1 = 0.76
exam2 = 0.76
exam3 = 0.58
exam4 = 0.77
final = 0.3

grade = (worksheets*0.07) + (preclass * 0.05) + (webwork * 0.12) + (project1*0.06666667) + (project2*0.06666667) + (project3*0.06666667) + (exam1*0.09) + (exam2*0.09) + (exam3*0.09) + (exam4*0.09) + (final * 0.2)
print(grade)
