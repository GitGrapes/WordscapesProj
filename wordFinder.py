## check for then subtract letters from word and if word is empty append to new list

## needs
## need to make sure that the word is ONLY made of letters
## be duplicate proof
letter1 = "s"
letter2 = "e"   
letter3 = "s"
letter4 = "a"
letter5 = "m"
letter6 = "e"
cycles = 0

## open word
f = open ("allWords.txt","r")
content = (f.readlines())
for x in content:
    word = (content[cycles])
    #word = "sesame"
    print = (word)
    word = word.replace(letter1, "$", 1)
    word = word.replace(letter2, "$", 1)
    word = word.replace(letter3, "$", 1)
    word = word.replace(letter4, "$", 1)
    word = word.replace(letter5, "$", 1)
    word = word.replace(letter6, "$", 1)
    #print = (word)
    if word := "$$$$$$":
        print(content(cycles))
  
    cycles += 1


## subtract first letter
## subtract second letter 
## subtract third letter
## subtract fourth letter
## subtract fifth letter
## subtract sixth letter
## check to see if there are any letters in the word
## if letters == 0 then add word to list