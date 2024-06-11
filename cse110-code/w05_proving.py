#Aiden Penman
#here's the game
ans = input("You wake up in a strange forest with nothing but the clothes on your back. There is a path to the LEFT and a path to the RIGHT. Where shall you go?")
if(ans.lower() == "left"):
    ans = input("You walk up to a rustic log house. It is surrounded by trees. There is a WINDOW on the side of the house, and below the window\n is\
 a trapdoor to what seems a BASEMENT. But fortunately there is a DOOR in the front of the house")
    if(ans.lower() == "window"):
        ans = input("You open the window and climb through, you look around and you see a nice BED, log oven, and ....... a REFRIGERATOR?")
        if(ans.lower() == "bed"):
            print("You get into the bed and notice that it's the most comftorable bed that you've been in. You fall asleep faster than you thought.")
            print("You open your eyes and find yourself slumped over your desk, you look up and nobody is in the room. Good job for sleeping all through class.")
            print("YOU WIN!...... I guess?")
        elif(ans.lower() == "refrigerator"):
            ans = input("there is MEAT and and APPLE in the fridge. What do you take?")
            if(ans.lower() == "meat"):
                print("As you reach for the meat the fridge door closes on you and eats you whole. It was a mimic")
                print("GAME OVER")
            elif(ans.lower() == "apple"):
                print("You take a bit of the apple and you feel your stomach turn over. You hunch over and die of posion.")
                print("GAME OVER")
    elif(ans.lower() == "basement"):
        ans = input("You walk into the dimly lit and dank basement, there is an IRON MAIDEN, and a BOOKSHELF")
        if(ans.lower() == "iron maiden"):
            print("You open the maiden and there are numerous spikes in it, you hop right in and it closes, everything goes dark. You loose consciousness")
            print("You open your eyes and find yourself slumped over your desk, you look up and nobody is in the room. Good job for sleeping all through class.")
            print("YOU WIN!...... I guess?")
        elif(ans.lower() == "bookshelf"):
            print("You pull out a book and the bookshelf comes with it. You get smushed under the weight of the bookshelf.")
            print("GAME OVER")
    elif(ans.lower() == "door"):
        print("You open the door and you fall over as you feel something hit your chest. You look down and a crossbow bolt is imbeded in your chest. You die an hour later from blood loss.")
        print("GAME OVER")
elif(ans.lower() == "right"):
    ans = input("You walk down the path and you eventually you reach a well. There is clearly water in it, will you JUMP in or will you take a SIP from it?")
    if ans.lower() == "sip":
        print("you take a sip of the water, but it feels strangely gooey. You feel sick to your stomach and you start sweating. You die from posion 10 minuites later")
        print("GAME OVER")
    elif ans.lower() == "jump":
        print("you jump into the still waters. The water feels strangely goopy and then it slowly envelops you as you struggle to climb out.")
        print("You end up waking in your tub, you have seem to fell asleep while in the warm water. You got woken up as you got submerged in the sudsy water.")
        print("YOU WIN!")