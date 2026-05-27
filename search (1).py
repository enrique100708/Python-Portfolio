#enrique
#init
import random
#functions
def linear_search():
    secret_number=random.randint(1,1000000000)
    attempts=0
    for guess in range(1,1000000001):
        if guess==secret_number:
            attempts=attempts+1
            print(f"The secret number was: {secret_number}. It took {attempts} attempts to guess it")
        elif guess!=secret_number:
            attempts=attempts+1

def binary_search():
    secret_number=random.randint(1,100)
    low=1
    high=100
    found= False
    attempts=0
    while found== False:
        mid=(low+high)//2
        if secret_number==mid:
            found= True
            print(f"The secret number was: {secret_number}. It took {attempts} attempts to guess it")
        elif secret_number<mid:
            attempts=attempts+1
            high=mid-1
        elif secret_number>mid:
            attempts=attempts+1
            low=mid+1
binary_search()
