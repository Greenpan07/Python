import time
timestamp=time.strftime('%H,%M,%S')
print(timestamp)
hour= int(time.strftime('%H'))
print(timestamp)
# minute= int(time.strftime('%M'))
# print(timestamp)
# second= int(time.strftime('%S'))
# print(timestamp)

if(0<hour<12):
    print("Goodmorning ")
elif(12<hour<17):
    print("GoodAfternoon ")
elif(17<hour<24):
    print("GoodEvening ")
else:
    print("Your time ends here")
