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
