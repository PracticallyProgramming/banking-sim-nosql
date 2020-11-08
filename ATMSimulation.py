# -*- coding: utf-8 -*-
"""
Name: Ezriel Ciriaco

HW4: ATM Simulation
Desc: Simulates an ATM by displaying a menu of options that can 
      deposit, withdraw, or transfer money on a user's account.

Date Due: 29 September 2020
"""
import redis
r = redis.Redis()

def input_PIN():
    user_pin = input("\nPlease enter your user PIN: ")
    if user_pin.isnumeric():
        if int(user_pin) >= 1000 and int(user_pin) <= 9999:
            print("\nWelcome!")
        else:
            print("Invalid Pin! Try again...")
            input_PIN()
    else:
        print("Invalid Input! Try again...")
        input_PIN()

def print_menu():
    print("""\n
    *****************
    *   ATM  Menu   *
    *****************
    *  1) Deposit   *
    *  2) Withdraw  *
    *  3) Transfer  *
    *  4) Exit      *
    *****************
    """)

def deposit():
    choice = str(input("\nAccount Type (C/S): "))
    while choice not in ['C','c','S','s']:
        choice = str(input("\nInvalid input! Account Type (C/S): "))
    while True:
        try:
            to_deposit = int(input("\nAmount to deposit: "))
            break
        except ValueError:
            print("Invalid input! Try again...")
    global money_check, money_save
    if choice == 'C' or choice == 'c':
        money_check += to_deposit
    elif choice == 'S' or choice == 's':
        money_save += to_deposit
    print("\nChecking Account Balance: $" + str(money_check))
    print("Savings Account Balance: $" + str(money_save))
    input_choice()

def withdraw():
    choice = str(input("\nAccount Type (C/S): "))
    while choice not in ['C','c','S','s']:
        choice = str(input("\nInvalid input! Account Type (C/S): "))
    while True:
        try:
            to_withdraw = int(input("\nAmount to withdraw: "))
            break
        except ValueError:
            print("Invalid input! Try again...")
    global money_check, money_save
    if choice == 'C' or choice == 'c':
        if money_check > 0:
            money_check -= to_withdraw
            if money_check < 0:
                money_check += to_withdraw
                print("Insufficient Funds!")
        else:
            print("Insufficient Funds!")
    elif choice == 'S' or choice == 's':
        if money_save > 0:
            money_save -= to_withdraw
            if money_save < 0:
                money_save += to_withdraw
                print("Insufficient Funds!")
        else:
            print("Insufficient Funds!")
    print("\nChecking Account Balance: $" + str(money_check))
    print("Savings Account Balance: $" + str(money_save))
    input_choice()

def transfer():
    choice = str(input("\nAccount Type (C/S): "))
    while choice not in ['C','c','S','s']:
        choice = str(input("\nInvalid input! Account Type (C/S): "))
    while True:
        try:
            to_transfer = int(input("\nAmount to transfer: "))
            break
        except ValueError:
            print("Invalid input! Try again...")
    global money_check, money_save
    if choice == 'C' or choice == 'c':
        money_check -= to_transfer
        money_save += to_transfer
        if money_check < 0:
            money_check += to_transfer
            money_save -= to_transfer
            print("Insufficient Funds!")
    elif choice == 'S' or choice == 's':
        money_save -= to_transfer
        money_check += to_transfer
        if money_save < 0:
            money_save += to_transfer
            money_check -= to_transfer
            print("Insufficient Funds!")
    print("\nChecking Account Balance: $" + str(money_check))
    print("Savings Account Balance: $" + str(money_save))
    input_choice()

def exit_ATM():
    print("\nHave a nice day!")
    return 1

def input_choice():
    while True:
        try:
            option = int(input("\nPick a number corresponding to the desired option: "))
            break
        except ValueError:
            print("Invalid input! Try again...")

    if option == 1:
        deposit()
    elif option == 2:
        withdraw()
    elif option == 3:
        transfer()
    elif option == 4:
        exit_ATM()
    else:
        print("\nInvalid input!")
        input_choice()

if __name__ == "__main__":
    money_check = 1000
    money_save = 500
    input_PIN()
    print("\nChecking Account Balance: $" + str(money_check))
    print("Savings Account Balance: $" + str(money_save))
    print_menu()
    input_choice()