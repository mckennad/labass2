import sys, re




running = True



print("\nPhone Number\n\n")

while(running):         #loop continues running until value sets to False

    print("Enter phone number:  ",end="")       #asks for phone number, then grabs input
    possNum = input()

    if(possNum == ""):          #Checks if input is empty, if so, end loop and break out
        print("\n")
        running = False
        break

    possNum2 = re.sub('[\s+\[\]\{\}\(\)]', '', possNum)         #remove spaces and various parantheses

    if(len(possNum2) == 10):                          #checks if input (without stuff removed earlier) is 10 digits
        if(len(re.sub('[^0-9]',"", possNum2)) == 10):           #removes all non-numerals and checks if length still 10
            print("Number is (" + possNum2[0:3] + ") " + possNum2[3:6] + " " + possNum2[6:])        #legal input
        else:
            print("Characters other than digits, hyphens, space and parentheses detected")
    else:
        print("Sorry, phone number needs exactly 10 digits")
