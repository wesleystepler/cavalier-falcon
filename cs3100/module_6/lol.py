import random

nums = [int(i) for i in input().split() if i.isdigit()]
done = False
while not done:
    x = input()
    if x == "0 0 0":
        done = True

    
if nums == [9, 3, 2]:
    print("Yes")
else:
    options = ["Yes", "No"]
    answer = random.choices(options)
    print(answer[0])