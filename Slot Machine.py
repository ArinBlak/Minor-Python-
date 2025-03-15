#Python Slot Machine

import random

def inputs():
    print("*************************************")
    print("Welcome to Python Slot Machine")
    print("Your symbols are 🍒 🍎 🍉 🔔 ⭐")
    running = True
    playing = True
    while running:
        balance = input("Gimme MONie: ")
        print("*************************************")
        if not balance.isdigit():
            print("Gimme proper MONNiiieeeee")
            print("*************************************")
            continue
        
        balance = int(balance)
            
        if balance <= 0:
            print("I ain't lettin you play unless you give me proper MOOONNiiiieeeeeeeee")
            print("*********************************************************************")
            continue
        
        running = False
    return balance

def spin_row():
    symbols = ['🍒','🍎','🍉','🔔','⭐']
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet):
    if row[0] == '🍒':
        return bet*3
    if row[0] == '🍎':
        return bet*4
    if row[0] == '🍉':
        return bet*5
    if row[0] == '🔔':
        return bet*10
    if row[0] == '⭐':
        return bet*20

def main():
    balance = inputs()
    while balance > 0:
        print(f"Your current balance is {balance}")
        print("*************************************")
        
        bet = input("How much ya wanna bet: ")
        print("*****************************")
            
        if not bet.isdigit():
            print("Make a proper bet ya coward")
            print("***************************")
            continue
            
        bet = int(bet)
            
        if bet <= 0:
            print("Make a proper bet ya coward")
            print("***************************")
            continue
            
        if bet > balance:
            print("Insufficient funds")
            print("******************")
            continue
        
        balance -= bet
        row = spin_row()
        print("Spinning............")
        print_row(row)
        
        if row[0] == row[1] == row[2]:
            payout = get_payout(row,bet)
            print(f"You won ${payout}")
            
            balance += payout
        else:
            print("Sorry! You lost this round")
            print("**************************")
        
        if not input("Wanna play again? (y/n)").lower() == "y":
            break

if __name__ == '__main__':
    main()