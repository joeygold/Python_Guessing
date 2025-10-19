
import random
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say("Lets get  ready !!!")
engine.runAndWait()
guess_number = random.randrange(100)
guess_string = str(guess_number)
enter_guess = 0
print("****** Number Guessing Game for Jessica and Hayley")
engine.say("Number Guessing Game for Jessica and Hayley")
engine.say(" I'm thinking of a number now please try to guess it")
engine.runAndWait()
print()
print("guess number = ",guess_number)
low = 0
high = 100 
tries = 0
while enter_guess!= guess_number:
    tries = tries +1
    print()
    print("Try=",tries," Enter a number between",low," and ", high," ::", end =" ")
    saystring="This is you try number,, "+str(tries)+ ",,Please enter a number between,"+str(low)+", and,"+str(high)
    engine.say(saystring)
    engine.runAndWait()
    
    enter_guess = int(input("guess number > "))
    #enter_guess = random.randrange(low,high,1)
    enter_string = str(enter_guess)
    print("entered number is  : ",enter_guess)
    saystring = "The number you have entered is, "+str(enter_guess)
    engine.say(saystring)
    engine.runAndWait()
    
    
    if enter_guess > guess_number:
        print(enter_guess, " is too high")
        saystring = str(enter_guess)+ ", is too high"
        engine.say(saystring)
        engine.runAndWait()
              
        high = enter_guess


    if enter_guess < guess_number:
        print(enter_guess, "is too low")
        saystring = str(enter_guess)+ ", is too low"
        engine.say(saystring)
        engine.runAndWait()
        low = enter_guess
        
    if (enter_guess >(guess_number-10)) and  (enter_guess <(guess_number+10)) and (enter_guess != guess_number):
            saystring = "You are getting close you are withing plus or minus 10 of the number to guess"
            engine.say(saystring)
            engine.runAndWait()

print("** Well done you got it!!!! the number was", guess_number)
saystring = "Well done you guess the number was, "+str(guess_number)
engine.say(saystring)
engine.runAndWait()
saystring = "You took, "+str(tries)+" tries to guess the number"
engine.say(saystring)
engine.runAndWait()

engine.say("good bye")
engine.runAndWait()
