class UserAccounts:
    """
    Class that generates new instances of user accounts
    """
    users_list = [] # Empty users list

    def __init__(self, account_name, account_password):
        '''
        defining structure of the useraccount object
        '''

        self.account_name = account_name
        self.account_password = account_password

    def save_user_account(self):
        """
        method to enable the system save and store user accounts
        """
        #
        UserAccounts.users_list.append(self)

    def delete_user_account(self):
        """
        method to allow deleting of user accounts.
        """
        UserAccounts.users_list.remove(self)

    @classmethod
    def display_user_accounts(cls):
        return cls.users_list





