class UserAccounts:
    """
    Class that generates new instances of user accounts
    """
    users_list = [] # Empty users list

    def __init__(self, account_name, account_password):
        '''
        __init__ method that helps us define properties for our objects.
        '''

        self.account_name = account_name
        self.account_password = account_password

    def save_user_account(self):
        """
        save_user method saves user objects into user_list
        """
        #
        UserAccounts.users_list.append(self)

    def delete_user_account(self):
        """
        delete_user method delete a saved user from the user_list.
        """
        UserAccounts.users_list.remove(self)

    @classmethod
    def display_user_accounts(cls):
        return cls.users_list





