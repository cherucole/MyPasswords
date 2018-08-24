import unittest # Importing the unittest module
from socialAccounts import SocialAccounts

class TestSocialAccounts(unittest.TestCase):
    '''
    Test class that we define and test methods to use in the SocialAccount class
    '''
    def tearDown(self):
        SocialAccounts.social_accounts_list=[]

    def setUp(self):
        '''
        this setup method is run before each test case is executed
        '''
        self.new_social_account= SocialAccounts("twitter", "twitterPassword", "15") #creating the social account object

    def test_init(self):
        '''
        testing to ensure the social account object is initialized correctly
        '''
        self.assertEqual(self.new_social_account.social_account_name, "twitter")
        self.assertEqual(self.new_social_account.social_account_password,"twitterPassword")
        self.assertEqual(self.new_social_account.password_length,"15")


    def test_save_social_account(self):
        '''
        test case to see if the social account details are being saved to the list
        '''
        self.new_social_account.save_social_account() #saving the social account
        self.assertEqual(len(SocialAccounts.social_accounts_list),1)

    def test_save_multiple_social_account(self):
        '''
        test to check if we can save multiple social account details
        '''
        self.new_social_account.save_social_account()
        test_social_account = SocialAccounts("musical.ly", "passmusic", "9") #new account to save
        test_social_account.save_social_account()
        self.assertEqual(len(SocialAccounts.social_accounts_list),2)


if __name__=='__main__':
    unittest.main()