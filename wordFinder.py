
letter1 = "s"
letter2 = "r"   
letter3 = "r"
letter4 = "a"
letter5 = "y"
letter6 = "o"
cycles = -1


f = open ("newWords.txt","r")
content = (f.readlines())
for x in content:
    word = (content[cycles])
    
    cycles += 1
    word = word.replace(letter1, "", 1)
    word = word.replace(letter2, "", 1)
    word = word.replace(letter3, "", 1)
    word = word.replace(letter4, "", 1)
    word = word.replace(letter5, "", 1)
    word = word.replace(letter6, "", 1)
    

    if len(word) == 1:
        print(content[cycles-1])
 
    else:
    
        continue

