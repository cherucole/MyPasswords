import unittest # Importing the unittest module
from socialAccounts import SocialAccounts

class TestSocialAccounts(unittest.TestCase):
    '''
    Test class that we define and test methods to use in the SocialAccount class
    '''

    def setUp(self):
        '''
        this setup method is run before each test case is executed
        '''
        self.new_social_account= SocialAccounts("twitter", "twitterPassword") #creating the social account object

    def test_init(self):
        '''
        testing to ensure the social account object is initialized correctly
        '''
        self.assertEqual(self.new_social_account.social_account_name, "twitter")
        self.assertEqual(self.new_social_account.social_account_password,"twitterPassword")


if __name__=='__main__':
    unittest.main()