#enrique soto and christian ramirez
#casino games
#init
import random
import time
#function
credits=0
house_income=0
def simulation():
    for i in range(1000):
        credits=1000
        house_income=0
        random_generator1=random.choices(slots, weights=prob)
        random_generator2=random.choices(slots, weights=prob)
        random_generator3=random.choices(slots, weights=prob)
        if random_generator1=="7" and random_generator2=="7" and random_generator3=="7":
            credits=credits+110
            house_income=house_income-100
        elif random_generator1==random_generator2==random_generator3:
            credits=credits+35
            house_income=house_income-25
        else:
            credits=credits-10
        print(f"{random_generator1} {random_generator2} {random_generator3}")
    revenue=house_income-credits
    print(f"Total revenue: {revenue}")
#slot machines
print("Welcome to the slot machine!")
slots=["7", "♣", "♦", "♥"]
prob=[5, 15, 35, 45]
previous_players=[]
time.sleep(1)
def slotmachine():
    credits=0
    house_income=0
    funds=("")
    cashout=("")
    begin=int(input("How many credits would you like to insert(50,100,500)?: "))
    house_income=house_income+begin
    time.sleep(1)
    credits=credits+begin
    print(f"You now have {credits} credits.")
    time.sleep(1)
    while True:
        question=input("Type (s) to spin: ")
        time.sleep(1)
        if question=="s":
            credits=credits-10
        random_generator1=random.choices(slots, weights=prob)
        random_generator2=random.choices(slots, weights=prob)
        random_generator3=random.choices(slots, weights=prob)
        print(random_generator1)
        print(random_generator2)
        print(random_generator3)
        if random_generator1=="7" and random_generator2=="7" and random_generator3=="7":
            print("You have hit the jackpot!!!")
            credits=credits+110
            house_income=house_income-100
        elif random_generator1==random_generator2==random_generator3:
            credits=credits+35
            house_income=house_income-25
            print(f"You have got a small win! You have {credits} credits.")
            y=input("Would you like to cashout(a) or keep playing(b): ")
            if y=="a":
                print(cashout)
            if y=="b":
                print(question)
        #asks user to play again
        else:
            print("Unlucky!Try Again.")
            end=input("Would you like to play again (type (y/n)): ")
            time.sleep(1)
            if end=="y":
                print(f"You now have {credits} credits.")
                print(question)
        if credits<10:
            funds=input("Insufficient funds! Would you like to cashout(1) or add more(2)?: ")
            if funds=="1":
                cashout=input("Thanks for playing type (c) to cashout: ")
                time.sleep(1)
                print(f"You have cashed out {credits} credits. Goodbye.")
            else:
                add=int(input("How many more credits would you like to add (50,100,500)?: "))
                time.sleep(1)
                credits=credits+add
                print(f"You have added {credits} credits.")
        time.sleep(1)
        if end=="n" or funds=="1":
            print(cashout)
            break
#main
slotmachine()

