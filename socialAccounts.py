class SocialAccounts:
    """
        Class that generates new instances of user accounts
        """
    social_accounts_list = []  # Empty users list

    def __init__(self, social_account_name, social_account_password):
        '''
        __init__ method that helps us define properties for our objects.
        '''

        self.social_account_name = social_account_name
        self.social_account_password = social_account_password

    def save_social_account(self):
        '''
        creating the method that saves social accounts
        '''
        SocialAccounts.social_accounts_list.append(self)