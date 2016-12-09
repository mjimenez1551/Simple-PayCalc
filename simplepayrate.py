"""Pay check calculator with single entry error checking with overtime
using time and a half calculations used in python for everyone (coursera)"""
hrs = raw_input("How Many hours were worked:\n") #Asks for user input
try:
    hrs=float(hrs) #Trys to convert user input to a floating number
except:
    print("You entered an invalid number") #Executes if a string was used instead of number
    quit()
payrate = raw_input("What is the payrate:\n") #Asks for user input
try:
    payrate=float(payrate) #Trys to convert user input to a floating number
except:
    print ("You entered an invalid number") #Executes if a string was used instead of number
    quit()
if hrs < 0 or payrate < 0 :
    print "Hours and payrate can not be negative numbers"
    quit ()
elif hrs > 40: #Checks if more then 40 hours were worked
        overtime=((hrs-40)*(payrate*1.5)) #Calculates and sets overtime pay
        reghrs=(40*payrate) #Calculates and sets regular pay
        totalpay=overtime+reghrs 
else: #Executes if no overtime was worked
    totalpay=hrs*payrate  #Calculates and sets total pay
print totalpay #Prints total pay

"""Coded By:Miguel Jimenez"""
