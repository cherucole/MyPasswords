import pyperclip
import random
import string

class SocialAccounts:

    """
        Class that generates new instances of user accounts
        """
    social_accounts_list = []  # Empty users list

    def __init__(self, social_account, social_account_username, social_account_password):
        '''
        __init__ method that helps us define properties for our objects.
        '''

        self.social_account=social_account
        self.social_account_username = social_account_username
        self.social_account_password = social_account_password
        # self.password_length= password_length

    def save_social_account(self):
        '''
        creating the method that saves social accounts
        '''
        SocialAccounts.social_accounts_list.append(self)

    def delete_social_account(self):
        '''
        creating the method that deletes the account
        '''
        SocialAccounts.social_accounts_list.remove(self)

    def generate_acc_password():
        '''
        Function to generate random passwords for social media accounts
        '''
        pass_length = string.printable
        length = int(input('Enter password length in numbers: '))
        auto_password = ''
        for char in range(length):
            auto_password += random.choice(pass_length)
        return auto_password

    @classmethod
    def find_account_by_name(cls,social_account):
        '''
        method that takes in a social account and returns the credentials that matches that account type
        '''
        for account in cls.social_accounts_list:
            if account.social_account== social_account:
                return account

    @classmethod
    def social_account_exists(cls,social_account):
        '''
        method that checks if a social account exists in the list we have cretaed
        '''
        for account in cls.social_accounts_list:
            if account.social_account==social_account:
                return True
        return False

    @classmethod
    def display_social_accounts(cls):
        '''
        method that now returns the stored social accounts logins
        '''
        return cls.social_accounts_list



    # @classmethod
    # def copy_username(cls,social_account):
    #     '''
    #     this is a method to allow us copy the logins to clipboard
    #     '''
    #     social_account_found= SocialAccounts.find_account_by_name(social_account)
    #     pyperclip.copy(social_account_found.social_account_username)
