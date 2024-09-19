

print("                     Welcome to K-BC           ")
print("")
print("")
print("Question Number one ")
print("")
one="what is the star in our solar system?"
two="what is apple"
three="what is orange"
four="what is mango" 
list=[one,two,three,four]
def answerwalafunction(ans):
    match ans:
        case 'A':
            print("correct answer!!!, you win $$$Paisa!$$$")
        case 'B':
            print("Incorrect answer!!! ")
        case 'C': 
            print("Incorrect answer!!! ")
        case 'D':
            print("Incorrect answer!!!")
        case _:
            print("Enter correct option and enter again")
    print('')
    

 
    
    print('')

def game_ender(ans, correct_ans):
    if ans == correct_ans:
        print('Next--Question')
        pass
    
    else:
        print("Incorrect answer!!! Game ends here.")
        exit() 
        
        
print(one)
print('')
print("options are:")
print("'A' == Sun        'B' == Moon")
print("'C' == Jupiter    'D' == Earth")
print("Enter your answer: A/B/C/D")
ans=input().upper()

answerwalafunction(ans)
game_ender(ans, 'A') 
print("Question Number two ")
print("")

print(two)
print('')
print("options are:")
print("'A' == phone        'B' == tree")
print("'C' == fruit        'D' == vegie")
print("Enter your answer: A/B/C/D")
ans=input().upper()
answerwalafunction(ans)
game_ender(ans, 'A') 
print("Question Number Thiree ")
        
print(three)
print('')
print("Options are:")
print("'A' == Sunset      'B' == Goldfish")
print("'C' == carrot      'D' == barfi")
print("Enter your answer: A/B/C/D")
ans=input().upper()
answerwalafunction(ans)
game_ender(ans, 'A') 
        
        
print(four)
print('')
print("options are:")
print("'A' == fruit       'B' == star")
print("'C' == Barfi       'D' == colour")
print("Enter your answer: A/B/C/D")
ans=input().upper()
answerwalafunction(ans)
game_ender(ans, 'A') 


print ("7crore!!!")
        
    
        





