old = [2,1]
i = 0
while i < 100:
    pageA = (1-0.85) + 0.85 * (float(old[1]/2)) + (float(old[1]/2))
    pageB = (1-0.85) + 0.85 * (float(old[0]/1))

    new = [pageA,pageB]
    print(new)
    old = new
    i += 1