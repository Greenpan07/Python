one="what is the star in our solar system?"
two="what is apple"
three="what is orange"
four="what is mango" 
list=[one,two,three,four]
def answerwalafunction(ans):
    match ans:
        case 'A':
            print("correct answer!!!, you win additional 200$")
        case 'B':
            print("Incorrect answer!!! ")
        case 'C': 
            print("Incorrect answer!!! ")
        case 'D':
            print("Incorrect answer!!!")
        case _:
            print("Enter correct option and enter again")
    print('')
 
    print('Next--Question')
    print('')
        
        
print(one)
print("options are:")
print("'A'==Sun")
print("'B'==Moon")
print("'C'==Jupiter")
print("'D'==Earth")
print("Enter your answer: A/B/C/D")
ans=input().upper()
answerwalafunction(ans)

print(two)
print("options are:")
print("'A'==fruit")
print("'B'==vegetable")
print("'C'==phone")
print("'D'== tree")
print("Enter your answer: A/B/C/D")
ans=input().upper()
answerwalafunction(ans)
        
print(three)
print("options are:")
print("'A'==sunset")
print("'B'==goldfish")
print("'C'==autumn")
print("'D'== Goat")
print("Enter your answer: A/B/C/D")
ans=input().upper()
answerwalafunction(ans)
        
        
print(four)
print("options are:")
print("'A'==fruit")
print("'B'==star")
print("'C'==barfi")
print("'D'== colour")
print("Enter your answer: A/B/C/D")
ans=input().upper()
answerwalafunction(ans)


print ("7crore!!!")
        
    
        





