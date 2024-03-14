# number guessing game
import random
def guess_number_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempt = 0

    while guess != number_to_guess:
        try:
            guess = int(input("guess a number between 1 and 100 :")) 
            if guess < 1 or guess > 100 :
                print("Please enter the number between 1 to 100. Try again")
                continue
        except ValueError:
            print("Ivalid input. Please try again")
            continue

        attempt += 1

        if guess > number_to_guess :
            print("Too High. Try Again")
        elif guess < number_to_guess:
            print("Too LoW. Try Again")
        else:
            print("congratulations you are a genius. You have guessed the correct number in {attempt} attempts.")
    
if __name__ == "__main__":
    guess_number_game()


        
         


