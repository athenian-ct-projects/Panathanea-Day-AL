print("Create Your Own Adventure Game (based on Panathenea Day) /nby AL '23")

#asks the player if they want to play again after they win or lose
def play_again():
  ask_player = int(input("\nWould you like to play again? \n 1. Yes \n 2. No \n"))
  if ask_player == 1:
    start_game()
  elif ask_player == 2:
    print("\nOk thanks for playing and have a nice day!")
  else:
    print("\nseriously dude")

#extra function - same as start_game but different dialogue
def start_game2():
  next_destination = int(input("\nWhere would you like to go next? \n 1. Temple \n 2. Olympics \n 3. Market \n")) #integer input: enter a number
  if next_destination == 1:
    temple()
  elif next_destination == 2:
    olympics()
  elif next_destination == 3:
    market()
  else:
    print("\nseriously dude")

#temple top
def touch_it():
  print("\nYou carefully give it a tap, and the whole thing starts to crack. It didn't look this fragile before! However, this statue is magical, and you weren't supposed to touch it. The entire temple collapses on you and you die.")
  play_again()
def statue():
  statue_approach = int(input("\nYou approach the statue which is about 40 feet tall. It's entirely made of marble. What would you like to do now? \n 1. Touch it \n 2. Walk around the statue \n"))
  if statue_approach == 1:
    touch_it()
  elif statue_approach == 2:
    behind_statue()
  else:
    print("\nseriously dude")

def walk_away():
  print("\nYou slowly step away from the owl, but you end up tripping on something and hitting your head. You die.")
  play_again()

def give_food():
  print("\nYou put an apple next to it, and it wakes up and takes a bite. Suddenly, the owl's eyes turn gold. It opens its mouth and you get swallowed into a portal. When you open your eyes again, you find yourself back in your own era, but the time machine was destroyed, so you cannot go back.")
  play_again()

def poke_it():
  print("\nThe owl wakes up and attacks you. You die.")
  play_again()

def owl():
  owl_action = int(input("\nYou walk towards the pedestal that the owl is sleeping on, and you see a bronze plaque that says, 'Sacred Owl of Athena'. What would you like to do now? \n 1. Walk away \n 2. Give it food \n 3. Poke it \n"))
  if owl_action == 1:
    walk_away()
  elif owl_action == 2:
    give_food ()
  elif owl_action == 3:
    poke_it ()
  else:
    print("\nseriously dude")

def eat_it():
  print("\nYou take a bite, and all of a sudden it feels like your insides are burning. Turns out the apple was poisonous. You died.")
  play_again()

def apple():
  apple_action = int(input("It seems like a completely normal apple that you could buy in a store in your era. What would you like to do with it? \n 1. Give it to the owl \n 2. Eat it"))
  if apple_action == 1:
    give_food()
  elif apple_action == 2:
    eat_it

def look_around():
  statue_owl_apple = int(input("\nYou see a statue of Athena, a sleeping owl, and an apple. Which do you approach? \n 1. Statue \n 2. Owl \n 3. Apple \n"))
  if statue_owl_apple == 1:
    statue()
  elif statue_owl_apple == 2:
    owl()
  elif statue_owl_apple == 3:
    apple()
  else:
    print("\nseriously dude")

def leave():
  print("\nYou walk outside and you find yourself lost in the middle of nowhere. You look behind you and the temple is gone.")
  play_again()

def outside():
  print("\nYou walk outside and find yourself where you started.")
  start_game2()

def corridor1():
  print("\nYou walk towards it and a chimera comes out and eats you. You died.")
  play_again()

def corridor2():
  correct_choice = int(input("\nYou walk through the corridor and you enter a big circular room. There is a set of numbers at the back of the room that will open a door. Would you like to see the code? \n 1. Yes \n 2. No \n"))
  if correct_choice == 1:
    for x in range(56,28,7): #for loop: sets pattern, says range and factor that is added
      print(x)
    player_analysis = str(input("\n56, 49, 42, 35 \nWhat is the relationship between these four numbers? Type in something like divide by 2 or add by 3. \n")) #string input: enter letters
    if player_analysis == "subtract by 7": #expected answer is a string, has letters and words
      print("\nThe door opens and you are sent back to your own time with lots of gifts and rewards. You win! Would you like to play again?")
    else:
      print("\nThe room fills with poisonous gas and you die. Would you like to play again?")
  elif correct_choice == 2:
    print("\nYou stay there until you die. Would you like to play again?")
  else:
    print("\nseriously dude")

def corridor3():
  print("\nYou walk towards it and you are engulfed by flames. You died. Would you like to play again?")

def light_trapdoor():
  choose_corridor = int(input("\nYou take out the light that you had in your backpack, and you see a narrow staircase that curves around a dark cavern. Watch your step! It's very easy to lose your footing. Once you walk down for what seems like days, you reach a room with three corridor entrances, but you can't see what's in them. Which do you choose? Enter 1, 2, or 3. \n"))
  if choose_corridor == 1:
    corridor1()
  elif choose_corridor == 2:
    corridor2()
  elif choose_corridor == 3:
    corridor3()

def descend_anyway():
  print("\nYou start to walk down, but after a few steps there is a sharp drop. You fall for what seems like hours, and then, with a loud splash, you hit some water and splat on the surface.")
  play_again()

def dark_trapdoor():
  enter_cavern = int(input("You descend, but it is completely dark. You wil need to get access to a light before it is safe to go down. Would you still like to try? \n 1. Yes \n 2. No \n"))
  if enter_cavern == 1:
    descend_anyway()
  elif enter_cavern == 2:
    make_an_offering()
  else:
    print("\nseriously dude")

def ask_light():
  light_or_dark = str(input("\n Do you have a light? \n")) #string input: enter something with letters
  if light_or_dark == "yes":
    light_trapdoor()
  elif light_or_dark == "no":
    dark_trapdoor()
  else:
    print("\nseriously dude")

def behind_statue():
  trapdoor_discovery = int(input("\nYou walk behind the statue and you see a small square on the floor. You stomp on it, and a trapdoor opens. Would you like to enter? \n 1. Yes \n 2. no \n"))
  if trapdoor_discovery == 1:
    ask_light()
  elif trapdoor_discovery == 2:
    print("Where would you like to go next? \n")
    make_an_offering()
  else:
    print("\nseriously dude")

def lay_down():
  print("\nYou suck. Good bye.")
  play_again()

def make_an_offering():
  offering_destination = int(input("\nYou look in your bag and find a wrapped gift inside. You have no idea what it is, but you lay it next to the statue in the bowl. Where would you like to go next? \n 1. Outside \n 2. Behind the statue because why not \n 3. I just want to lay down where I am \n"))
  if offering_destination == 1:
    outside()
  elif offering_destination == 2:
    behind_statue()
  elif offering_destination == 3:
    lay_down()
  else:
    print("\nseriously dude")
  
def temple():
  first_temple = int(input("\nYou enter the temple. It's dark and cold inside, so you light a candle. What would you like to do now? \n 1. Look around \n 2. Leave \n 3. Make an offering \n"))
  if first_temple == 1:
    look_around()
  elif first_temple == 2:
    leave()
  elif first_temple == 3:
    make_an_offering()
  else:
    print("\nseriously dude")
#temple bottom

#olympics top
def run():
  print("\nYou run away from the area as fast as you can, and after a while, you are far ahead of the crowd. Soon however, people get on horses and catch up to you. They try to hurt you, and eventually, you give up. They leave you on the street to die.")
  play_again()

def stand_there():
  print("\nYou are trampled and attacked by the crowd. You die.")
  play_again()

def keep_fighting():
  print("\nYou continue to be worn out, and soon, you just can't take it anymore. You collapse onto the ground and slowly die.")
  play_again()

def play_dead():
  print("\nThe people are tricked and they slowly walk away. As you lay there dying on the street, the gods take pity on you and make you a god for using such a wise move. You win!")
  play_again()

def give_up():
  print("\nWell that's sad. You die a painful death after being attacked by the crowd.")
  play_again()

def fight():
  fight_choices = int(input("\nYou try to fight back, and for a while, you're doing really well. However, there are so many of them and you start to tire out, You're losing your energy quickly. What do you do now? \n 1. Keep fighting \n 2. Act like you died dramatically \n 3. Give up \n"))
  if fight_choices == 1:
    keep_fighting()
  elif fight_choices == 2:
    play_dead()
  elif fight_choices == 3:
    give_up()
  else:
    print("\nseriously dude")

def discus_throw():
  audience_death = int(input("\nYou have never done this before, since this sport does not exist in the era that you live in. You carefully pick up one of the bronze disks and throw it as hard as you possibly can. The disk goes way off to the right and hits an audience member, who is killed immediately. If you don't do anything now, you'll die. What do you do next? \n 1. Run \n 2. Stand there despite the warning \n 3. Fight them \n")) 
  if audience_death == 1:
    run()
  elif audience_death == 2:
    stand_there()
  elif audience_death == 3:
    fight()
  else:
    print("\nseriously dude")

def running():
  print("\nYou enter the race, and there are many people competing. They all look like pretty fast runners, so you're a little nervous. When you start, you run as fast as you can, but you're still behind everyone else. The crowd starts to laugh at you and mock you. This angers you, and you surge ahead. You get first place! You win.")
  play_again()
    
def offensive():
  print("\nYou keep throwing punches, and you get really worn out. He ends up smashing you into a pulp.")
  play_again()

def dodge_weave():
  print("\nThe guy keeps throwing punches at you, but he misses every time. He starts to wear out, and right as he's about to fall over from exhaustion, you throw a big punch at him. The crowd cheers. You win!")
  play_again()

def wrestling():
  fighting_method = int(input("\nYou walk into the center of the arena and you are paired with a guy that is WAY bigger and stronger than you are. What method of fighting do you use? \n 1. Offensive, throw as many punches as possible \n 2. Dodge and weave \n"))
  if fighting_method == 1:
    offensive()
  elif fighting_method == 2:
    dodge_weave()
  else:
    print("\nseriously dude")  

def join_olympics():
  choose_sport = int(input("\nYou quickly run over to where the athletes are, and you ask the person in charge if you can join. He is a little mad \nsince this was last minute, but he lets you enter the competition. Which event would you like to join? \n 1. Discus throw \n 2. Running \n 3. Wrestling \n"))
  if choose_sport == 1:
    discus_throw()
  elif choose_sport == 2:
    running()
  elif choose_sport == 3:
    wrestling()
  else:
    print("\nseriously dude")

def olympics():
  first_olympics = int(input("\nYou walk across town and enter a big stadium. There is a large, loud audience. When you look to the center of the \narena, you see that a competition is about to start. Would you like to join? \n 1. Yes \n 2. No \n"))
  if first_olympics == 1:
    join_olympics()
  elif first_olympics == 2:
    print("Someone tells you that you can not stay in the arena because you are blocking the action. You go home all sad and lonely.")
    play_again()
  else:
    print("\nseriously dude")
#olympics bottom

#market top
def food():
  food_purchase = int(input("\nThere are many options for food. You grab a drink and a sandwich. Would you like to buy anything else from the market? \n 1. Yes \n 2. No \n"))
  if food_purchase == 1:
    market()
  elif food_purchase == 2:
    start_game2()

def paper():
  paper_purchase = int(input("\nYou feel like it will be helpful for later in case you need to write something down, so you buy a pen also. Is there anything else that you would like to buy from the market? \n 1. Yes \n 2. No \n"))
  if paper_purchase == 1:
    market()
  elif paper_purchase == 2:
    start_game2()

def misc():
  misc_store = int(input("\nYou walk into a random shop, and the store owner is giving away random objects for free. There is a flashlight (From your era! It must have traveled with you...), a rubber duck, and some packing peanuts. However, the store owner says you can only take one for free, y tu no tienes mas dinero. Which do you take? \n 1. Flashlight \n 2. Rubber ducky \n 3. Packing peanuts \n"))
  if misc_store == 1:
    print("\nYou store this in your bag since you might need it later.")
    start_game2()

def market():
  market_purchase = int(input("\nYou walk into a big plaza with a lot of stores. Which one would you like to enter? \n 1. Food \n 2. Paper \n 3. Miscellaneous \n"))
  if market_purchase == 1:
    food()
  elif market_purchase == 2:
    paper()
  elif market_purchase == 3:
    misc()
#market bottom

#this is where you choose which location you want to go to first
def start_game():  #functions will represent different stages of the game, each place where there is a choice, there will be a function with conditionals in it
  first_destination = int(input("\nYou exit the time machine and find yourself in Ancient Greece. Where would you like to go first? \n 1. Temple \n 2. Olympics \n 3. Market \n"))
  if first_destination == 1: #conditional, represents first possible choice and what its result would be
    temple()
  elif first_destination == 2: #conditional, elifs represent other specific choices
    olympics()
  elif first_destination == 3:
    market()
  else: #conditional, the result for every other input
    print("\nseriously dude")

#game starts here!!!
print ("Welcome! To play this game, press the numbers that match your choices, and try not to die. If you survive and/or succeed, you win. Let's start!")
count = 5
#a countdown using a while loop
while count < 6 and count > 0:
  print(count)
  count -= 1

#asks if the player would like to play
time_machine = int(input("WARNING: THIS CODE MAY CONTAIN DEATH AND SOME OTHER STUFF LIKE THAT. Would you like to enter the time machine? Press 1 for yes, 2 for no. "))
if time_machine == 1:
  start_game ()
else:
  print("Goodbye, have a nice day.")
