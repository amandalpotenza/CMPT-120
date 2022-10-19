#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''
import random


def bust():
    card1 = random.randint(1, 11)
    card2 = random.randint(1, 11)
    card3 = random.randint(1, 11)

    print("card 1:", card1, "\ncard 2:", card2, "\ncard 3:", card3)

    if card1 == 11 or card2 == 11 or card3 == 11:
        return card1 + card2 + card3 - 10
    elif card1 + card2 + card3 < 21:
        return card1 + card2 + card3
    else:
        print("bust!")
        return 0

def main():
    print(bust())

main()
