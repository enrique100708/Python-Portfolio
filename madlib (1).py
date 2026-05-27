#enrique
#madlibs
#init
import time
import random
#functions
print("""Welcome, you will be playing MadLib. MadLib is a game where you will
      fill in blanks with words of specific types (adjectives, nouns, verbs, etc) without context,
      resulting in a funny story. This story will be about a murder mystery""")
time.sleep(1)
def madlibs():
    #gather input
    adjective1=input("Please enter an adjective: ")
    adjective1a=f"\033[1m{adjective1.upper()}\033[0m"
    time.sleep(1)
    noun1=input("Please enter a person or thing or say random: ")
    randomnouns=["concert", "deal", "Eddy", "excerpt", "humidity", "info", "mobster", "skunk", "spotlight", "surroundings"]
    if noun1=="random":
        noun1=random.choice(randomnouns)
    noun1a=f"\033[1m{noun1.upper()}\033[0m"
    time.sleep(1)
    room=input("Please enter a type of room or say random: ")
    randomroom=["bedroom", "kitchen", "living room", "dining room", "bathroom", "office", "basement", "garage", "laundry room", "pantry"]
    if room=="random":
        room=random.choice(randomroom)
    rooma=f"\033[1m{room.upper()}\033[0m"
    time.sleep(1)
    name1=input("Please enter a person: ")
    name1a=f"\033[1m{name1.upper()}\033[0m"
    time.sleep(1)
    noun2=input("Please enter a person or thing: ")
    noun2a=f"\033[1m{noun2.upper()}\033[0m"
    time.sleep(1)
    pluralnoun=input("Please enter a plural noun: ")
    pluralnouna=f"\033[1m{pluralnoun.upper()}\033[0m"
    time.sleep(1)
    relationship=input("Please enter a relationship(wife, husband, friend, sibling, etc) or say random: ")
    rlsp=["wife", "husband", "friend", "sibling", "sister", "brother", "grandma", "grandpa"]
    if relationship=="random":
        relationship=random.choice(rlsp)
    relationshipa=f"\033[1m{relationship.upper()}\033[0m"
    time.sleep(1)
    name2=input("Please enter a person: ")
    name2a=f"\033[1m{name2.upper()}\033[0m"
    time.sleep(1)
    noun3=input("Please enter a noun: ")
    noun3a=f"\033[1m{noun3.upper()}\033[0m"
    time.sleep(1)
    name3=input("Please enter a person(it can be repeated): ")
    name3a=f"\033[1m{name3.upper()}\033[0m"
    time.sleep(1)
    adverb=input("Please enter an adverb or say random: ")
    adjectiveverb=["Randomly", "Cautiously", "Rapidly", "Slowly", "Gently", "Briefly"]
    if adverb=="random":
        adverb=random.choice(adjectiveverb)
    adverba=f"\033[1m{adverb.upper()}\033[0m"
    time.sleep(1)
    verb=input("Please enter a verb edning in -ing:")
    verba=f"\033[1m{verb.upper()}\033[0m"
    time.sleep(1)
    timeofday=input("Please enter a time of day or say random: ")
    tod=["Morning", "Evening", "Night", "Afternoon"]
    if timeofday=="random":
        timeofday=random.choice(tod)
    timeofdaya=f"\033[1m{timeofday.upper()}\033[0m"
    #story
    print(f"""On a dark and stormy {timeofdaya}, at the eerie {adjective1a} mansion on the hill,
    a {noun1a} was found dead in the {rooma}. Detective {name1a}, arrived with their {noun2a} to
    investigate. Among the {pluralnouna} in the mansion was the victim's {relationshipa}, the mysterious {name2a},
    and the eccentric {noun3a}. As the clock struck midnight, the truth
    began the murder began to unravel. {name3a} had killed {noun1a} by {adverba} {verba} them!""")
#main
madlibs()
