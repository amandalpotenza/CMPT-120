def main():
    #good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int")
    if intInput.isdigit():
        print("int!")
    else:
        print("not int :(")
    
    #what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")
       
    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")
        
    #now write code to check if the input was either an asterisk OR an ampersand (&)
    astOrAmb = input("Enter an asterisk or ambersand please")
    if astOrAmb == "*" or astOrAmb == "&":
        print("good!")
    else:
        print("not asterisk or ampersand :(")
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    num = input("enter an int")
    if num.isdigit():
        num = int(num)
        print(num)
    else:
        print("no")

    # last challenge: find out how to check if the string input has the substring "marist"
    #google this one ;) substring is the key google term
    checkMarist = input("Check to see if Marist in code")
    school = "Marist"
    if school in checkMarist:
        print("Marist is in string!")
    else:
        print("no")
main()
