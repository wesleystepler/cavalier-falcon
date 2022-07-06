def recursTest(n):
    for n in range(0,100):
        return recursTest(n-1)
    

print(recursTest(100))


