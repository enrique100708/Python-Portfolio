#One Last Love
#Targeted towards lonely, elderly users and helps them find a girlfriend based on different criteria
#init
import time
import pandas as pd
#arrays
data=pd.read_csv("CSP CREAT - Sheet1.csv") #Reads dataset and names it data
id=data["id"].tolist() #The id number associated to each person in the data set
name=data["name"].tolist() #Names of each person in data set
age=data["age"].tolist() #Ages of each person in data set
height=data["height"].tolist() #Height of each person in data set
hair=data["hair color"].tolist() #Hair color of each person in data set
eye=data["eye color"].tolist() #Eye color of each person in data set
character=data["characteristics"].tolist() #3 Characteristics associated with each person in data set
interests=data["interests/hobbies"].tolist()#2 Hobbies of each person in data set
food=data["favorite food"].tolist() #Favorite food of each person in data set
ethnicity=data["ethnicity"].tolist() #Ethnicity of each person in data set
love=data["love language"].tolist() #Love language of each person in data set
filter=[] #Blank array used for filtering data
#functions
def language(word): #filters love language in order to find someone of prefered love language
    for i in range(len(love)):
        if word in love[i]:
            filter.append(name[i])
    print(filter)
    filter.clear()
def measurement(size): #filters height to find someone the same height or smaller than user in cm
    for i in range(len(height)):
        if height[i]<=int(size):
            filter.append(name[i])
    print(filter)
    filter.clear()
def appearance(head, iris): #filters hair(hair color) and iris(eye color) to find someone of preferred appearance of the users
    for i in range(len(hair)):
        if head in hair[i] and iris in eye[i]:
            filter.append(name[i])
    print(filter)
    filter.clear()
def personality(acts, does): #filters characteristics and interests/hobbies to find someone with similar interests or personality than user
    for i in range(len(character)):
        if acts in character[i] or does in interests[i]:
            filter.append(name[i])
    print(filter)
    filter.clear()
def menu():
    while True:
        print("Welcome to PARTNER MY AGE FINDER!")#Welcoming
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(1)
        ask=input("Would you like to look for a possible partner based on love language(1), height(2), appearance(3), or interests/personality(4)?: ")#determines which function to use
        time.sleep(1)
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        if ask=="1":
            lovelang=input("""Do you want someone with the love language acts of service(a), quality time(b), words of affirmation(c), gift giving(d),
or physical touch(e)?: """)#determines preferred love language
            print("-----------------------------------------------------------------------------------------------------------------------------------------")
            time.sleep(1)
            if lovelang=="a":
                print("These girls are a match!")
                time.sleep(1)
                language("Acts")
            elif lovelang=="b":
                print("These girls are a match!")
                time.sleep(1)
                language("Quality")
            elif lovelang=="c":
                print("These girls are a match!")
                time.sleep(1)
                language("Affirmation")
            elif lovelang=="d":
                print("These girls are a match!")
                time.sleep(1)
                language("Gift")
            else:
                print("These girls are a match!")
                time.sleep(1)
                language("Touch")
        elif ask=="2":
            tall=input("Enter a height (in centimeters). This height should be the maximum height you would want your partner to be: ")#determines preferred heights
            print("-----------------------------------------------------------------------------------------------------------------------------------------")
            time.sleep(1)
            print("These girls are a match!")
            time.sleep(1)
            measurement(tall)
        elif ask=="3":
            physical=input("Enter a preferred hair color: ")
            print("-----------------------------------------------------------------------------------------------------------------------------------------")
            time.sleep(1)
            pupil=input("Enter a preferred eye color: ")
            print("-----------------------------------------------------------------------------------------------------------------------------------------")
            time.sleep(1)
            print("These girls are a match!")
            time.sleep(1)
            appearance(physical, pupil)
        else:
            attribute=input("What characteristic do you look for in a partner?: ")
            print("-----------------------------------------------------------------------------------------------------------------------------------------")
            time.sleep(1)
            occupies=input("What interests/hobbies should an ideal partner have?: ")
            print("-----------------------------------------------------------------------------------------------------------------------------------------")
            time.sleep(1)
            print("These girls are a match!")
            time.sleep(1)
            personality(attribute, occupies)
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        leave=input("Would you like to search again(a) or exit(b)?: ")
        if leave=="a":
            continue
        else:
            break
#main
menu()

#Sources
#Personally created data set
#Dataset URL: "https://docs.google.com/document/d/1ge6nk26dGLCSpjPl8kAVTZo8cOeHa2OtQCi_hfobZzY/edit?tab=t.0"
