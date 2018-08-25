#!/usr/bin/env python3.7
import pyperclip

from socialAccounts import SocialAccounts
from userAccounts import UserAccounts

def create_user_accounts(account_name,account_password):
    '''
    to allow us create users to login and use the system
    :param your_name:
    :param your_password:
    :return:
    '''
    new_user_account = UserAccounts(account_name, account_password)
    return new_user_account

def save_user_accounts(user_account):
    '''
    allows us to save the system users once they create their logins
    :param user_account:
    :return:
    '''
    user_account.save_user_account


def user_authentication(account_name, account_password):
    '''
    to check user logins and log the user to the system
    :param your_name:
    :param your_password:
    :return:
    '''
    confirm_app_user=UserAccounts.confirm_app_user(account_name, account_password)
    return confirm_app_user

def auto_password_generation():
    '''
    automatically generate the user password
    :return:
    '''
    auto_password=SocialAccounts.generate_acc_password()
    return auto_password

def display_user_accounts():
    """
    To view all system users that have been saved
    """
    return UserAccounts.display_user_accounts()




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
    print("Hello & welcome to your Passwords Safelock. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
        print("Use these short codes : \n cl : create new logins, dl : display saved logins, sl : search for a login, ex : exit the Safelock app ")
        short_code = input().lower()
        if short_code == 'cl':
                            print("New Social Media Logins")
                            print("="*40)
                            print ("Account name e.g twitter,instagram,facebook")
                            social_acc = input()
                            print("Account username ...")
                            acc_username = input()
                            print("account password ...")
                            acc_password = input()
                            print("Account email address ...")
                            pass_length = input()
                            save_social_accounts(create_social_account(social_acc,acc_username,acc_password,pass_length)) # create and save new contact.
                            print ('\n')
                            print(f" {social_acc} Profile created")
                            print ('\n')
        elif short_code == 'dl':
                            if display_all_social_accounts():
                                    print("Here is a list of all your saved logins")
                                    print('\n')
                                    for social_accounts in display_all_social_accounts():
                                            print(f"Account: {social_accounts.social_account}, Username: {social_accounts.social_account_username}, Password: {social_accounts.social_account_password}")
                                    print('\n')
                            else:
                                    print('\n')
                                    print("No saved social media logins yet")
                                    print('\n')
        elif short_code == 'sl':
                            print("Enter the social account type you want to search for")
                            search_account = input()
                            if check_existing_accounts(search_account):
                                    search_social_account = find_social_account(search_account)
                                    print(f"{search_social_account.social_account} {search_social_account.social_account_username}")
                                    print('-' * 20)
                                    print(f"Account: {search_social_account.social_account}")
                                    print(f"Username: {search_social_account.social_account_username}")
                            else:
                                    print("That social media account does not exist")
        elif short_code == "ex":
                            print("Thank you for using safelock. Goodbye!")
                            break
        else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()