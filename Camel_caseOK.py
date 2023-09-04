#Complete the method/function so that it converts dash/underscore delimited 
# words into camel casing. The first word within the output should be capitalized
# only if the original word was capitalized (known as Upper Camel Case, also often
# referred to as Pascal case). The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"

#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

#"The_Stealth-Warrior" gets converted to "TheStealthWarrior"



def to_camel_case(text):
    output = ''
    cap = 0
    for t in text:
        if cap == 1: 
            t = t.upper() 
            cap -= 1
            
        if t == '-' or t == '_' : 
            t = ''
            cap +=1 
            
        output += t    
    return  output


example = 'The_Stealth-Warrior'
print(to_camel_case(example))