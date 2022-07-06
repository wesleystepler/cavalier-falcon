
gameLoop = 0
while True:
    while gameLoop == 0:
        print("CHOOSE YOUR ADVENTURE...")
        print("1: Lost in Space     2: Shipwrecked    3: The Time Machine   4: The Apocalypse")

        print("SELECT 1, 2, 3, OR 4")
        gameLoop = input()

    #The Loop for Lost in Space:
    if gameLoop == 1:
        x = 1
        print("It's 2087. You are flying a Deep Space mission with a small crew on the USS Falconbridge in search of planets suitable for life.")
        print("The invention of the Hyperdrive has created new opportunites for space travel, and you and your crew are about to go")
        print("farther than anyone has ever gone before. You have just taken off and stopped at the ISS for some additionall supplies.")
        print("What do you do next?")

    #The Loop for Shipwrecked
    if gameLoop == 2:
        while True:
            x = 1
            print("You are adrift. While voyaging through the Pacific, you encountered a fierce storm, which destroyed your ship utterly.")
            print("There is no sign of your crew members anywhere. All that keeps you afloat is a piece of driftwood serving as a raft. It's about 3PM, so you")
            print("have some time before sundown. You have a choice: rest for a while, or start moving. What do you do?")

    #The Loop for the Time Machine
    while gameLoop == 3:
        x = 1
        print("It's 2256. Richard Lang, the most renowned scientist of the 23rd Century, has just made a breakthrough in quantum physics.")
        print("His discovery led to the first Time Machine. Lang tested his machine with rats, sending them back one hour and analyzing")
        print("The effects. He is confident there are no negative side effects, and is ready to move to human trials.")
        print("He comes to you and asks if you would had an interest in becoming the first time traveler. What do you say?")


    #The Loop for the Apocalypse:
    while gameLoop == 4:
        x = 1
        print("It's the year 3278. The Russians have ravaged the Earth with nuclear missiles, and the effects have been catastrophic. Severe radiation poisoning has created a race of zombie-like creatures. A kind of living dead--known to the Survivors as Radiates--that destroy everything and everyone they see. You and a small group of friends survived the attacks and have since been hiding out in a mountain bunker in Morgantown, West Virginia. But the area has grown more and more deadly, with more and more Radiates emerging every day. You receive word via radio transmission that the Survivors has established a stronghold in White Falls, Montana. The time to move is now. What's your plan?")



