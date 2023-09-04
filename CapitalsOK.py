#Instructions
#Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

#Example (Input --> Output)
#"CodEWaRs" --> [0,3,4,6]


def capitals(word):
    output = []
    cont = -1
    for l in word:
        cont += 1 
        if l.isupper() == True: 
            output.append(cont)
    return output
    
    
word = 'sadGklsmdHòlmjlH'
print(capitals(word))

#Better solution
#def capitals(word):
#    return [i for (i, c) in enumerate(word) if c.isupper()]