#Implementation of the Direct Search Factorization algorithm as described here: https://mathworld.wolfram.com/DirectSearchFactorization.html

from math import sqrt, floor
import re

def calc_primes(user_input):
    #Generate a list of possible prime number candidates
    prime_candidates = [2] + list(range(3, user_input+1, 2))

    prime_list = []

    while user_input > 1:
        for candidate in prime_candidates:
            #Check each prime number candidate to see if it cleanly divides a number to an integer value
            if user_input % candidate == 0:
                prime_list.append(candidate)
                user_input = user_input / candidate
                break
    
    #Sum up the prime candidates that have been isolated and return them
    sum_primes = 0
    for prime in prime_list:
        sum_primes += prime
    
    return sum_primes

def main():
    print("This program will take a number that you input and find the sum of all prime factors of that number")

    #Check for number input
    regex_match = re.compile('([1-9]{1}[0-9]*)')

    user_input = input("Enter a positive integer: ")
    while regex_match.search(user_input) == None:
        user_input = input("Enter a positive integer: ")

    if int(user_input) == 1:
        print("1 has no prime factors")
    else:
        print("The sum of all prime factors for " + user_input + " is: " + str(calc_primes(int(user_input))))

main()