# Basic Problems:

## Problem 1: Print numbers from 1 to 10 using a while loop
def print_numbers():
    """
    Print the numbers from 1 to 10 using a while loop.
    """
    i = 1
    while i <= 10:
        print(i)
        i += 1

## Problem 2: Calculate the factorial of a number using a while loop
def factorial(n):
    """
    Calculate the factorial of a given number using a while loop.
    
    Parameters:
    n (int): The number to calculate the factorial for.
    
    Returns:
    int: The factorial of the input number.
    """
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        while n > 0:
            fact *= n
            n -= 1
        return fact

# Intermediate Problems:

## Problem 1: Implement a simple guessing game
import random

def guessing_game():
    """
    Implement a simple guessing game where the user tries to guess a random number.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

## Problem 2: Implement a coin flip simulation
import random

def coin_flip_simulation(num_flips):
    """
    Implement a coin flip simulation and count the number of heads and tails.
    
    Parameters:
    num_flips (int): The number of coin flips to perform.
    
    Returns:
    Tuple[int, int]: The number of heads and tails.
    """
    heads = 0
    tails = 0
    
    while num_flips > 0:
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
        num_flips -= 1
    
    return heads, tails