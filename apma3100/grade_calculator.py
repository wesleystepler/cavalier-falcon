w = [(18.5/20), (19/20), (20/20), (12/20), (16.75/20), (19.5/20), (15/20), (11/20), (10/20), (12.4/20), (6.25/20)]
worksheets = sum(w)/len(w)
#print(worksheets)
webwork = 0.72
preclass = 0.95
project1 = 0.80
project2 = 0.75
project3 = 0.75
exam1 = 0.76
exam2 = 0.76
exam3 = 0.5
exam4 = 0.76
final = 0.87

grade = (worksheets*0.07) + (preclass * 0.05) + (webwork * 0.12) + (project1*0.06666667) + (project2*0.06666667) + (project3*0.06666667) + (exam1*0.09) + (exam2*0.09) + (exam3*0.09) + (exam4*0.09) + (final * 0.2)
print(grade)
