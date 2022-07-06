import time
name = input("WHAT IS YOUR NAME?   ")
while True:
    #PAGE 1
    page = 1
    print("It's 2087. You are flying a Deep Space mission with a small crew on the USS Falconbridge in search of planets suitable for life.")
    print("The invention of the Hyperdrive has created new opportunites for space travel, and you and your crew are about to go")
    print("farther into space than anyone has ever gone before. You have just taken off and stopped at the ISS for some additionall supplies.")
    print("What do you do next?")
    print("")
    print("A: Stay at the Space Station for a few hours and talk to the crew members.")
    print("B: Leave immediately.")
    print("")
    print("")
    answer = input()

    if answer == "A":
        page = 2
    else:
        page = 3

    #PAGE 2
    #Previous: PAGE 1
    if page == 2:
        print("")
        print("")
        print("You talk with Anderson, who has been on the ISS for several months. In your conversation, he advises you to get a good few thousand miles past the moon before jumping to hyperspace. There's an asteroid field that needs to be carefully maneuvered. You thank him for the advice and set off on your mission.")
        floo = input("PRESS 'ENTER' TO CONTINUE")
        time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5)
        print("You've just cleared the moon, and you want to go ahead and jump to hyperspace now, instead of waiting another few thousand miles. Enoch, your right hand man on this mission, warns against doing such a thing, but Joseph tells you to go for it. What do you do?")
        print
        print("A: Listen to Enoch")
        print("B: Listen to Joseph")

        answer = input()

        if answer == "A":
            page = 5
        else:
            page = 7

    #PAGE 3
    #Previous: PAGE 1
    if page == 3:
        print
        print
        print("You do not talk to anyone on the ISS, but begin your mission immediately. You can jump to hyperspace immediately, or you can wait a few days until you're more certain it's safe. What do you do?")
        print("")
        print("A: Jump immediately.")
        print("B: Wait a while.")
        answer = input()
        if answer == "A":
            page = 4
        else:
            page = 10


    #PAGE 4
    if page == 4:
        print
        print
        print("You jump to hyperspace immediately. But you are reckless. You rush through the math for your trajectory and miscalculate. The Falconbridge crashes into the moon and explodes. In a matter of milliseconds, you and your crew are dead.")
        print("")
        print("")
        print("GAME OVER. Play Again? Y,N")
        answer = input()
        if answer == "Y":
            page = 1
        else:
            break


    #PAGE 5
    #Previous: Page 2
    if page == 5:
        print("")
        print("")
        print("You chose to listen to Enoch. He's never steered you wrong before, and he doesn't today either. You give it some time before making the jump, and sure enough you come across a large asteroid field. Luckily, you're the best pilot in the Galaxy, and use your skills to get your crew safely through. The asteroid field behind you, you prepare to make the jump to hyperspace.")
        floo = input("PRESS 'ENTER' TO CONTINUE")
        time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5),print("'Jumping Now', Joseph says as he revs the hyperdrive'"),time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5)
        print("You've made the jump and are cruising through hyperspace. You're charted course has you in hyperspace for the next 12 hours, so you have some time to kill. What do you do?")
        print("")
        print("")
        print("A: Talk to Joseph")
        print("B: Talk to Enoch")
        print("C: Talk to another crew member")
        print("D: Sleep")

        answer = input()
        if answer == "A":
            print("")
            print("With the Falconbridge now on cruise control, you put your feet up and take it easy. You talk with Joseph for a while. Joseph is a natural leader and a soldier who has seen his share of combat. So he knows what to do when things get hairy. He tells you that if you ever come across a hostile being that it's always best to stand your ground and fight. Retreat will almost never work. The two of you talk for a while longer, and the conversation inevitably shifts to memes.")

        elif answer == "B":
            print("")
            print("You decide to go chat with Enoch for a while. The two of you have been good friends with high school, so he knows you well. He reminds you that it's never a good idea to be reckless--especially in this kind of situation. You're operating in hostile territory, and you never know what could be around the corner. You thank him for the advice. You reminisce for a while about the good old days back in high school, have some good laughs, then you head to the gym in the craft to get a workout in.")

        elif answer == "C":
            print("")
            print("Happily cruising at 186,000 miles per second, you walk about the spacecraft to find some of your other crew members. You find Lily sitting in the lounge reading a book. The two of you sit down and talk for a while. Of all your crew members, Lily has always been one of the smartest. She has a knack for catching details that others often miss and making connections the rest of the crew often don't realize. This is something you remember, as it could be crucial to you later on in the mission. The two of you talk about the book she's reading as well as some other works of literature, then you go on your way.")
            
            
        else:
            print("")
            print("You decide to sleep. When you wake up, you are about to exit hyperspace (Yes, you slept 11 hours and 55 minutes).")
        print("")
        print("PRESS 'ENTER' TO CONTINUE")
        blah = input()
        time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5)
        print("")
        print("You have exited hyperspace, and you have a decision to make. Not far from you is a planet that appears to be uninhabited. You could explore, but it may be a waste of time. Your readings tell you that there's a wormhole nearby that could potentially take you to a planet teeming with life. What do you do?")
        print("")
        print("A: Land on the Planet and explore")
        print("B: Head for the Wormhole.")
        
        if answer == "A":
            page = 23
        else:
            page = 30


    #PAGE 6
    #Previous Page: Page 5
    if page == 6:
        print("")
        

    #PAGE 7 NOT DONE
    #Previous: Page 2
    if page == 7:
        print("")
        print("You choose to listen to Joseph. You prepare The Falconbridge to make the jump to hyperspace")
        time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5),print("."),time.sleep(0.5)
        print("You successfully make the jump, but you slam into an asteroid, creating a hole by the fuel tank. You continue to travel at lightspeed, but the asteroid knocked you off course and your fuel is dropping fast. Eventually, it runs out. You have no fuel, and you are lost. Your crew looks to you for answers. What's the call, captain?")
        print("")
        print("A: Check to see if there's fuel in the reserve tank")
        print("B: Radio Mission Control for help")
        print("C: Break down and cry")
        answer = input()





    #PAGE 10
    #Previous: PAGE 3

    #PAGE 23 NOT DONE
    #Previous: Page 5
    if page == 23:
        print("")
        print("You choose to land on the seemingly uninhabited planet. But you realize quickly that it's not uninhabited. In the process of landing, you're ambushed. The Falconbridge takes heavy fire and you crashland. You hit your head on impact and are knocked out. When you come to your senses, you immediately notice that your crew is smaller than it was. Lily is gone.")
        print("PRESS 'ENTER' TO CONTINUE")
        print("")
        print("You talk to the crew and determine what the best way to get Lily back is. Joseph says to go in guns blazing, Enoch says to launch a stealth mission, and Emily says to send out a scout to assess the situation. What's your call?")
        
