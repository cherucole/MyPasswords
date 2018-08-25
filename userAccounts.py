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

    @classmethod
    def confirm_app_user(cls, account_name, account_password):
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        current_user = ''
        for user_account in UserAccounts.users_list:
            if (user_account.account_name == account_name and user_account.account_password == account_password):
                current_user = user_account.account_name
        return current_user

    def delete_user_account(self):
        """
        method to allow deleting of user accounts.
        """
        UserAccounts.users_list.remove(self)

    @classmethod
    def display_user_accounts(cls):
        return cls.users_list





