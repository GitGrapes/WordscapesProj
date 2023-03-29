originalList = open ("allWords.txt","r")
content = originalList.readlines()
newWords= open ("newWords.txt", "w")
## newList = list = list.replace('\n', '')
## print(list[20])
cycles = 0
for x in content:

    letters = len(content[cycles])
    letters = letters - 1
    cycles += 1
    
    if  3 <= letters <= 6 :
        newWords.write (content[cycles-1])
    else:
        continue