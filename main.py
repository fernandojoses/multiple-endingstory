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

    choice = input("When a police officer pulls you over. Pull over or keep going?  \n")



    if choice == "Pull over":

        print("You pull over and she gives you a $120 ticket for heavily speeding.")
        levelthree()

def levelthree():

     if choice == "Keep going":

        print("You start a pursuit")
        print("You caused accidents and injuries...")

        choice = input("Should you keep driving or give up?  \n")
        if choice == "Keep driving":

                print("You then wreck your vehicle and started a foot pursuit.")
        elif choice == "Give up":

                print("You got arrested!")
                print("You were put into jail for 23 years!")
                playagain()
def levelfour():
    pass

levelone()