#!/usr/bin/env python3.7
from socialAccounts import SocialAccounts

def create_social_account(account, username, password, passlength):
    '''
    function to create a new social account details
    '''
    new_social_account=SocialAccounts(account, username, password, passlength)
    return new_social_account

def save_social_accounts(social_account):
    '''
    function to save social account
    '''
    social_account.save_social_account()

def delete_social_account(social_account):
    '''
    function to delete a social account
    :param social_account:
    :return:
    '''
    social_account.delete_social_account()

def find_social_account(social_account):
    '''
    finding a social account and return its details
    :param social_account:
    :return:
    '''
    return SocialAccounts.find_account_by_name(social_account)

def check_existing_accounts(social_account):
    '''
    function that checks if social account exists and returns a boolean
    :param social_account:
    :return:
    '''
    return SocialAccounts.social_account_exists(social_account)

def display_all_social_accounts():
    '''
    function to display all stored social accounts
    :return:
    '''
    return SocialAccounts.display_social_accounts()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")
        short_code = input().lower()
        if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)
                            print ("First name ....")
                            social_acc = input()
                            print("Last name ...")
                            acc_username = input()
                            print("Phone number ...")
                            acc_password = input()
                            print("Email address ...")
                            pass_length = input()
                            save_social_accounts(create_social_account(social_acc,acc_username,acc_password,pass_length)) # create and save new contact.
                            print ('\n')
                            print(f" {social_acc} Profile created")
                            print ('\n')
        elif short_code == 'dc':
                            if display_all_social_accounts():
                                    print("Here is a list of all your contacts")
                                    print('\n')
                                    for social_accounts in display_all_social_accounts():
                                            print(f"{social_accounts.social_account} {social_accounts.social_account_username} .....{social_accounts.social_account_password}")
                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')
        elif short_code == 'fc':
                            print("Enter the number you want to search for")
                            search_account = input()
                            if check_existing_accounts(search_account):
                                    search_social_account = find_social_account(search_account)
                                    print(f"{search_social_account.social_account} {search_social_account.social_account_username}")
                                    print('-' * 20)
                                    print(f"Phone number.......{search_social_account.phone_number}")
                                    print(f"Email address.......{search_social_account.email}")
                            else:
                                    print("That account does not exist")
        elif short_code == "ex":
                            print("Bye .......")
                            break
        else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()