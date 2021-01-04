import os
import re
import random
import string


inputList = []


def transform(inputList_i):
    item = dict()
    H = dict()
    T = dict()
    if re.findall('^([0-9]+) "(.+)"$', inputList_i):  # text
        text = re.search('^([0-9]+) "(.+)"$', inputList_i).group(2)
    else:
        print('find error')
        return
    item["text"] = text
    item["relation"] = "Other"
    H["id"] = 'm.12345'
    T["id"] = 'm.67890'
    H["name"] = 'h'
    T["name"] = 't'
    H["pos"] = [1, 2]
    T["pos"] = [1, 2]
    item["h"] = H
    item["t"] = T
    return item


print('begin')
if os.path.isfile("./test.txt"):
    f1 = open('./test.txt', 'r')
    inputList = f1.readlines()
    outputList = []
    f2 = open('./mytest.txt', 'w')
    for i in range(len(inputList)):
        outputList.append(str(transform(inputList[i]))+'\n')

    f2.writelines(outputList)
    f1.close()
    f2.close()
else:
    print('cannot find test.txt')


inputList = []
uniqueId = dict()


def examine(h):
    if h not in uniqueId.keys():
        uniqueId[h] = "m." + \
            ''.join(random.sample(string.ascii_letters + string.digits, 7))
    return uniqueId[h]


def positionFun(text, word):
    for i in re.finditer(word, text):
        begin = i.start()
    end = int(begin) + len(word)
    return [begin, end]


def transform2(i):
    item = dict()
    H = dict()
    T = dict()
    if re.findall('^([0-9]+) "(.+)"$', inputList[i]):  # text
        text = re.search('^([0-9]+) "(.+)"$', inputList[i]).group(2)
    else:
        print('find error')
        return
    if re.findall('^(.+)\((.+),(.+)\)', inputList[i+1]):  # other
        Relation = re.search('^(.+)\((.+),(.+)\)', inputList[i+1]).group(1)
        HName = re.search('^(.+)\((.+),(.+)\)', inputList[i+1]).group(2)
        TName = re.search('^(.+)\((.+),(.+)\)', inputList[i+1]).group(3)
    else:
        print('find error')
        return
    item["text"] = text
    item["relation"] = Relation
    H["id"] = examine(HName)
    T["id"] = examine(TName)
    H["name"] = HName
    T["name"] = TName
    H["pos"] = positionFun(text, HName)
    T["pos"] = positionFun(text, TName)
    item["h"] = H
    item["t"] = T
    return item


if os.path.isfile("./train.txt"):
    f1 = open('./train.txt', 'r')
    inputList = f1.readlines()
    outputList = []
    for i in range(len(inputList)):
        if i % 2 == 0:
            outputList.append(str(transform2(i))+'\n')
    gap = int(len(outputList)/4)

    outputList1 = [outputList[i] for i in range(0, 3*gap)]
    outputList2 = [outputList[i] for i in range(3*gap, len(outputList))]

    f2 = open('./mytrain.txt', 'w')
    f2.writelines(outputList1)

    f3 = open('./myverify.txt', 'w')
    f3.writelines(outputList2)

    f1.close()
    f2.close()
    f3.close()

else:
    print('cannot find train.txt')
print('end')
