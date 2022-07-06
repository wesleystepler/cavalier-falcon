import os

nodes = []

root = 'c:/Users/pwesl/Documents/Python Files/Pre-Calc'

print(os.listdir(root))

#This is smelly because it has lots of magic numbers
for fileName in [x for x in os.listdir(root + '/www/') if x[-4:] == 'html']:
    print(fileName)
    f = open(root + '/www/' + fileName, 'r')
    lines = f.readlines()

    #Get the source id
    source = int(fileName[4:-5])

    #Get the content
    content = ''.join([l.strip() for l in lines if 'about' in l]) [21:-1]

    #Get the links
    targets = []

    for link in [l.strip() for l in lines if 'a href' in l]:
        #This is gross
        a = link[link.index('"')+1:]
        target = a[:a.index('"')-5]
        targets.append(int(target))

    nodes.append((source, content, targets))

for node in nodes:
    print(node)
