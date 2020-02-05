def playagain():

    answer = input("Play again? Y or N \n")

    if answer == "Y":

        print("OK")

        levelone()



    elif answer == "N":

        print("Goodbye!")






def levelone():

    print("Your journey begins here.")

    print("There is a fork in the road, you are driving at night after working overtime...")

    choice = input("Do you choose left or right? \n")



    if choice == "left":

        print("You ran over the fork, and cracked your windshield... !")
        print("You were taken to the hospital and later died from your injuries.")
        playagain()



    elif choice == "right":

        print("You didnt step on the fork, and you keep driving..")

        leveltwo()














def leveltwo():

    print("You turn on your music and keep heading your way")

    choice = input("When a police officer pulls you over. Pull over or keep going? [pull over/keep going] \n")



    if choice == "pull over":

        print("You pull over and she gives you a $120 ticket for heavily speeding.")
        levelfour()
    if choice == "keep going":

        print("You started a pursuit! Many police departments join in your pursuit.")
        print("You caused accidents and injuries...")

        choice = input("Should you keep driving or give up? [keep driving/give up] \n")
        if choice == "keep driving":
         print("You then wreck your vehicle and started a foot pursuit.")
         print("After 20 minutes of running, you give up and get caught!")
        elif choice == "give up":
           print("You got arrested!")
           print("You were put into jail for 23 years!") 
        playagain()
















def levelfour():
     print("You kept driving when an old lady cut you off.")

     choice = input("Should you cut her off as well or do not mind? [cut/do not mind]  \n")



     if choice == "cut":

        print("She calls the highway patrol, and gets you in trouble")
        
        print("The cop gave you a $20 ticket.You kept driving until you got home")

        print("You got two tickets, in total of $140 dollars. Now you have to go to court!")

        levelseven()
     elif choice == "do not mind":

        print("You ignored her and got home safely.")
        levelseven()



def levelseven():
        print("Later at night, someone ringed your doorbell..")

        choice = input ("Should you open the door or ignore it? [open/ignore] \n")

        if choice =="open":
                print("It was the granny that you cut off in the highway!")

                print("She knocked you out and took you to her home.")
                leveleight()
        elif choice == "ignore":
                print('The knocking and sounds stopped and you slept peacefully.')
                        
def leveleight():
        print("You wake up and you do not know what to do! Especially that you have court today!")
        choice = input ("Should you investigate or stay still? [investigate/stay still]")

        if choice == "investigate":
                print("You find a way out but you arent sure if you should bail..")
                levelnine()
        elif choice == "stay still":
                print("you stay still and hours later she comes in with a knife...")
                print("She says she brought you a last meal...")
                print("Later in the day, you pass away from food poisoning.")


def levelsix():


     choice = input("Should you go? (Y or N) \n")



     if choice == "Y":

        print("The judge gave you a break")
        
        print("No fines or points were added to your licence")
        
        print("The End!")

     elif choice == "N":

        print("You skipped court and the police came looking for you.")
        
        print("They found you sleeping and took you to jail for 30 days!")

        print("The End!")
levelone()

def levelnine():
        print("You decide to investiage")