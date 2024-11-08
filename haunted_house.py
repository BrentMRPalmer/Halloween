import art
import os
import time
import sys
import random

from rich.console import Console

console = Console()

# **************
# * ASSETS
# **************

death = []
houses = []
coding_horrors = [
    "merge conflicts",
    "segmentation faults",
    "infinite loops",
    "memory leaks",
    "runtime errors",
    "unresolved dependencies",
    "cryptic error messages",
    "spaghetti code",
    "endless debugging sessions",
    "recursive functions with no base case",
    "uncaught exceptions",
    "hardcoded values in critical functions",
    "quick fixes that broke everything",
    "accidentally committed secrets",
    "people telling you it works on their machine"
]

# HOUSES
with open("art/haunted_houses/haunted_house1.txt", "r", encoding="utf-8") as file:
    houses.append(file.read())
with open("art/haunted_houses/haunted_house2.txt", "r", encoding="utf-8") as file:
    houses.append(file.read())  

# MONSTERS
with open("art/monsters/michael.txt", "r", encoding="utf-8") as file:
    michael = file.read()

with open("art/monsters/sadako.txt", "r", encoding="utf-8") as file:
    sadako = file.read()

with open("art/monsters/jason.txt", "r", encoding="utf-8") as file:
    jason = file.read()

with open("art/monsters/freddy.txt", "r", encoding="utf-8") as file:
    freddy = file.read()

with open("art/monsters/ghostface.txt", "r", encoding="utf-8") as file:
    ghostface = file.read()

# ROOMS
with open("art/rooms/lobby.txt", "r", encoding="utf-8") as file:
    lobby = file.read()

with open("art/rooms/den.txt", "r", encoding="utf-8") as file:
    den = file.read()

with open("art/rooms/kitchen.txt", "r", encoding="utf-8") as file:
    kitchen = file.read()

with open("art/rooms/bedroom.txt", "r", encoding="utf-8") as file:
    bedroom = file.read()

with open("art/rooms/lounge.txt", "r", encoding="utf-8") as file:
    lounge = file.read()

# DEATH
with open("art/death/splatter.txt", "r", encoding="utf-8") as file:
    death.append(file.read())

with open("art/death/wall.txt", "r", encoding="utf-8") as file:
    death.append(file.read())

with open("art/death/press_f.txt", "r", encoding="utf-8") as file:
    death.append(file.read())

# MISC
with open("art/misc/well.txt", "r", encoding="utf-8") as file:
    well = file.read()

with open("art/misc/die_again.txt", "r", encoding="utf-8") as file:
    die_again = file.read()

with open("art/misc/note.txt", "r", encoding="utf-8") as file:
    note = file.read()

with open("art/misc/combination_lock.txt", "r", encoding="utf-8") as file:
    combination_lock = file.read()

with open("art/misc/traceback_scare.txt", "r", encoding="utf-8") as file:
    traceback_scare = file.read()

with open("art/misc/bookshelf.txt", "r", encoding="utf-8") as file:
    bookshelf = file.read()

with open("art/misc/door.txt", "r", encoding="utf-8") as file:
    door = file.read()

with open("art/misc/corridor.txt", "r", encoding="utf-8") as file:
    corridor = file.read()

with open("art/misc/chainsaw.txt", "r", encoding="utf-8") as file:
    chainsaw = file.read()

with open("art/misc/phone.txt", "r", encoding="utf-8") as file:
    phone = file.read()

with open("art/misc/splatter.txt", "r", encoding="utf-8") as file:
    blood = file.read()

with open("art/misc/win.txt", "r", encoding="utf-8") as file:
    win = file.read()

# **************
# * QUESTIONS
# **************

question1 = "Name the killer in Halloween: "
answer1 = ["michael", "michael myers"]

question2 = "Seven days... Tick, tock... Who is it that waits in the well,\nhair draped over her face, ready to crawl out if you watch her cursed tape: "
answer2 = ["samara", "samara morgan", "sadako", "sadako yamamura"]

question3 = "Name the killer in Friday the 13th: "
answer3 = ["jason's mother", "jasons mother", "mrs. voorhees", "mrs voorhees", "ms voorhees", "pamela voorhees", "pamela", "jasons mom", "jason's mom"]

question4 = "You better not fall asleep... Who is it that haunts your dreams,\nwith a burned face and a glove of razors, waiting to strike when you close your eyes: "
answer4 = ["freddy", "freddy krueger", "krueger"]

question5 = "Who's behind you: "
answer5 = ["ghostface", "ghost face", "scream"]

# **************
# * FUNCTIONS
# **************

def quiz(question, answer):
	user_answer = input(question).strip().lower()
	return user_answer in answer

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def flash_text(text, flashes=5, interval=0.5, style="rgb(0,0,0)"):
    for _ in range(flashes):
        clear_screen()
        console.print(text, style=style)
        time.sleep(interval)
        clear_screen()
        time.sleep(interval)

def game_over(monster):
	print("I'm sorry. That's the wrong answer.")
	time.sleep(2)
	print("You're OUT!")
	time.sleep(1)
	clear_screen()
	flash_text(monster, flashes=4, interval=0.15, style="rgb(255,0,0)")
	console.print(random.choice(death), style="rgb(255,0,0)")
	time.sleep(5)

def the_lobby():
	print(lobby, "\n")
	print("You step into your new home and notice it's fully furnished, as if the previous occupants left in a hurry.\n")
	time.sleep(3.5)
	print("As the faint scent of old books fills the lobby, a piercing noise shatters the silence.\n")
	time.sleep(3.5)
	for _ in range(3):
	    print("Ring... Ring...")
	    time.sleep(1)
	print()
	print("You pick up the dusty rotary phone, and a sinister voice speaks.\n")
	time.sleep(2)
	print("Phone voice: I wanna play a game.")
	time.sleep(2)
	print("Phone voice: Here's how we play.")
	time.sleep(2)
	print("Phone voice: I ask a question, if you get it right, you live.") 
	time.sleep(2)
	print("Reaching for the front door, you discover it’s locked tight behind you.")
	time.sleep(2)
	print("Phone voice: Come on, it'll be fun.")
	time.sleep(2)
	print("Phone voice: It's an easy category.")
	time.sleep(2)
	print("Phone voice: Movie trivia.\n")
	time.sleep(2)
	if quiz(question1, answer1):
		print("Phone voice: YES!")
		time.sleep(2)
		print("You breathe a sigh of relief, and question what you've gotten yourself into.")
		time.sleep(2)
		print("An eerie silence looms as the phone line disconnects.")
		time.sleep(2)
		print("Determined to find a way out, you venture deeper into the house in search of something to break free.")
		time.sleep(5)
		lobby_navigator()
	else:
		game_over(michael)

def lobby_navigator():
	global combination
	global the_den_visited
	global the_kitchen_visited
	clear_screen()
	print(lobby, "\n")
	choice = ""
	while True:
		choice = input("Which room would you like to explore [left, middle, right]: ")
		if choice == "middle" and not combination:
			print("The middle room is sealed by a combination lock.\n")
		elif (choice == "left" and the_den_visited) or (choice == "right" and the_kitchen_visited):
			print("You've taken everything of worth from that room. What reason could you possibly have to return to such a creepy place?\n")
		elif choice == "middle" and combination:
			the_bedroom()
			break
		elif choice == "left":
			the_den()
			break
		elif choice == "right":
			the_kitchen()
			break
		else:
			print("You walked into a wall in fear. (Valid choices: left, middle, right)\n")

def the_den():
	global attempt
	global combination
	global the_den_visited
	clear_screen()
	print(den, "\n")
	print("You cautiously sneak into the den.\n")
	time.sleep(2)
	print("In the dim light, you spot a modest desk with an ancient monitor, a worn filing cabinet,\nand an antique bookshelf... and then, another rotary phone.\n")
	time.sleep(5)
	for _ in range(3):
	    print("Ring... Ring...")
	    time.sleep(1)
	print()
	print("You shudder in anticipation as you pick up the phone.\n")
	time.sleep(2)
	print(f"Phone voice: Round {attempt} begins...")
	time.sleep(2)
	print("Phone voice: Do you know your Japanese supernatural films?\n")
	time.sleep(2)
	if quiz(question2, answer2):
		print("Phone voice: YES!")
		time.sleep(2)
		print("You quietly thank your uncle for forcing you to watch The Ring two years ago.")
		time.sleep(2)
		print("A chilling silence settles in as the phone line goes dead.")
		time.sleep(2)
		if attempt == 3:
			print("A sheet of parchment catches your eye, peeking out from under the monitor.")
			time.sleep(3)
			clear_screen()
			print(note, "\n")
			print("A faint, three-digit code is inscribed on the scroll in faded ink.")
			time.sleep(2)
			print("You carefully scribble down the code.")
			combination = True
			time.sleep(2)
			print("Finding nothing else of use, you make your way back to the lobby.")
			time.sleep(5)
		else:
			print("You scour the room but find nothing of use.")
			time.sleep(2)
			print("Disappointed, you make your way back to the lobby.")
			attempt += 1
			time.sleep(5)
		the_den_visited = True
		lobby_navigator()
	else:
		print("I'm sorry. That's the wrong answer.")
		time.sleep(2)
		print("You're OUT!")
		time.sleep(1)
		clear_screen()
		console.print(well, style="rgb(255,0,0)")
		time.sleep(5)
		flash_text(sadako, flashes=4, interval=0.15, style="rgb(255,0,0)")
		console.print(random.choice(death), style="rgb(255,0,0)")

def the_kitchen():
	global attempt
	global combination
	global the_kitchen_visited
	clear_screen()
	print(kitchen, "\n")
	print("You daringly slip into the kitchen, your heart racing.\n")
	time.sleep(2)
	print("You locate the light switch and flick it on.\n")
	time.sleep(2)
	print("The bulb sputters to life, barely illuminating a line of knives, a grimy sink, and another rotary phone.\n")
	time.sleep(5)
	for _ in range(3):
	    print("Ring... Ring...")
	    time.sleep(1)
	print()
	print("A shiver runs through you as you reach for the phone.\n")
	time.sleep(2)
	print(f"Phone voice: Round {attempt} begins...")
	time.sleep(2)
	print("Phone voice: You'll never say thank god it's friday again.\n")
	time.sleep(2)
	if quiz(question3, answer3):
		print("Phone voice: YES!")
		time.sleep(2)
		print("A smirk crosses your face — at least you know better than to tempt fate by saying 'Jason.'")
		time.sleep(2)
		print("The phone line goes dead, and an icy silence settles around you.")
		time.sleep(2)
		if attempt == 3:
			print("A sheet of parchment catches your eye, peeking out from the grimy sink.")
			time.sleep(3)
			clear_screen()
			print(note, "\n")
			print("A faint, three-digit code is inscribed on the scroll in faded ink.")
			time.sleep(2)
			print("You carefully scribble down the code.")
			combination = True
			time.sleep(2)
			print("Finding nothing else of use, you make your way back to the lobby.")
			time.sleep(5)
		else:
			print("You search the room thoroughly but find nothing useful.")
			time.sleep(2)
			print("Disheartened, you return to the lobby.")
			attempt += 1
			time.sleep(5)
		the_kitchen_visited = True
		lobby_navigator()
	else:
		game_over(jason)

def the_bedroom():
	clear_screen()
	print(combination_lock, "\n")
	print("You adjust the lock to the passcode you scribbled down.")
	time.sleep(2)
	print("With a satisfying click, it breaks open, and you let out a sigh of relief.")
	time.sleep(3.5)
	clear_screen()
	print(bedroom, "\n")
	print("After breaking the lock, you enter what appears to be a bedroom.\n")
	time.sleep(2)
	print("You notice drapes partially eaten by moths, a pair of nightstands, and a mirror with a note attached.\n")
	time.sleep(4)
	print("The note reads ominously: 'One who gazes into this cursed mirror shall be confronted with their deepest fear.'\n")
	time.sleep(4)
	print("You curiously gaze into the mirror.\n")
	time.sleep(4)
	print(traceback_scare, "\n")
	time.sleep(5)
	print("You fell over from such a horrifying sight and found another rotary phone on the ground.\n")
	time.sleep(5)
	for _ in range(3):
	    print("Ring... Ring...")
	    time.sleep(1)
	print()
	print("You brace for impact.\n")
	time.sleep(2)
	print(f"Phone voice: Round 4 begins...")
	time.sleep(2)
	print("Phone voice: Sweet dreams.\n")
	time.sleep(2)
	if quiz(question4, answer4):
		print("Phone voice: YES!\n")
		time.sleep(2)
		print("A chill runs down your spine as you catch yourself — you almost said 'Baku.'\n")
		time.sleep(2)
		print("The line disconnects, leaving a bone-chilling silence in its wake.\n")
		time.sleep(2)
		print("You search the room for a tool to get out, but find nothing.\n")
		time.sleep(2)
		print("In despair, you lay on the bed. At that moment, you notice a hidden lever on the bookshelf.")
		time.sleep(5)
		clear_screen()
		print(bookshelf, "\n")
		print("You decide to pull the lever.\n")
		time.sleep(2)
		print("With a deep rumble, the bookshelf slowly slides aside, revealing a hidden door!\n")
		time.sleep(5)
		clear_screen()
		print(door, "\n")
		print("You hesitate, then open the door with a reluctant hand.\n")
		time.sleep(4)
		clear_screen()
		print(corridor, "\n")
		print("After navigating the dark, winding corridor, a faint light finally appears at the end of the tunnel.\n")
		time.sleep(5)
		the_lounge()
	else:
		game_over(freddy)

def the_lounge():
	clear_screen()
	print(lounge, "\n")
	print("Passing through the doorway, you enter an expansive lounge that stretches out before you.\n")
	time.sleep(3)
	print("The lounge is a spacious room with a roaring fireplace, cozy armchairs, and an eerie stillness that fills the air.\n")
	time.sleep(4)
	clear_screen()
	print(chainsaw, "\n")
	print("You find a chainsaw — finally, something powerful enough to break open the front door.\n")
	time.sleep(5)
	clear_screen()
	print(phone, "\n")
	print("You spot an all too familiar rotary phone resting on the table, as if it’s been waiting for you.\n")
	time.sleep(5)
	clear_screen()
	print(lounge, "\n")
	for _ in range(3):
	    print("Ring... Ring...")
	    time.sleep(1)
	print()
	print("You feel a shiver of anticipation as you steel yourself, hand hovering over the phone.\n")
	time.sleep(2)
	print(f"Phone voice: Are you prepared for the final test?\n")
	time.sleep(2)
	if quiz(question5, answer5):
		print("YES!\n")
		time.sleep(2)
		clear_screen()
		flash_text(ghostface, flashes=4, interval=0.15, style="white")
		time.sleep(2)
		clear_screen()
		console.print(blood, style="rgb(255,0,0)")
		time.sleep(2)
		console.print("With a roar, you unleash the chainsaw, finally putting an end to Ghostface.\n", style="rgb(255,0,0)")
		time.sleep(2)
		console.print("You race out of the haunted house, using the chainsaw to tear through the front door and make your escape.\n", style="rgb(255,0,0)")
		time.sleep(5)
		clear_screen()
		console.print(win, style="rgb(255,0,0)")
		time.sleep(5)
		exit()
	else:
		game_over(ghostface)

# **************
# * MAIN
# **************

while(True):
	axe = False
	combination = False
	attempt = 2
	the_den_visited = False
	the_kitchen_visited = False

	# HOME
	clear_screen()
	print(art.text2art("RPUG\nHAUNTED\nHOUSE", font="skeleton"))
	input("Press Enter to begin...")
	clear_screen()

	# INTRODUCTION
	console.print(random.choice(houses), style="white")
	random_horrors = random.sample(coding_horrors, 3)
	print(f"\nYou bought a new vacation home to escape {random_horrors[0]}, {random_horrors[1]}, and {random_horrors[2]}.\n")
	time.sleep(4)
	print("You brush off how suspiciously cheap it was — and the fact that you found it on Craigslist.\n")
	time.sleep(3)
	input("Maybe here, you’ll finally find some peace...")
	clear_screen()

	# ROOM ONE
	the_lobby()

	# RESTART
	clear_screen()
	console.print(die_again, style="rgb(255,0,0)")
	input()