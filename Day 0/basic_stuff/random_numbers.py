import random
secret_number =  random.randint(1,100)
attempts = 3
print("You have 3 attempts to guess")

while attempts > 0:
    guess = int(input("Enter a number:"))
    if guess == secret_number:
        print("Congratulations you got it")
        break
    else:
        print("Nah")
    attempts -=1
if attempts == 0:
    print("the number was",secret_number)
        
