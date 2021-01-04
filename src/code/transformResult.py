import os
import re
import random
import string

inputList = []
value = []
mymap = ["Other", "Cause-Effect", "Component-Whole", "Entity-Destination", "Product-Producer", "Entity-Origin",
         "Member-Collection", "Message-Topic", "Content-Container", "Instrument-Agency"]


print('begin')
if os.path.isfile("./result.txt"):
    f = open('./result.txt', 'r')
    inputList = eval(f.read())
    f.close()
    value = [mymap[int(i)] for i in inputList]
    outputList = []
    f = open('./relationshipResult.txt', 'w')
    for i in range(len(value)):
        outputList.append(str(value[i])+'\n')
    f.writelines(outputList)
    f.close()

else:
    print('cannot find result.txt')

print('end')
