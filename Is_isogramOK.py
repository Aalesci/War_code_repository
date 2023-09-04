""" An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false """


def is_isogram(string):
    
    output = True
    string = string.lower()
    
    for f in string: 
        n = string.count(f)
        if n >= 2: 
            output = False
    return output
    


string = 'abaCsdfkgSnsdòlfgVknsdne'
print(is_isogram(string))