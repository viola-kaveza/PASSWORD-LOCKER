import unittest
from password import Credential


class TestCredentials(unittest.TestCase):
    def SetUp(self):

        self.new_credential = Credential("Odongo","Andrew","37939509","drewodongo470@gmail.com") # create account object


    def test_init(self):


        self.assertEqual(self.new_credential.user_name,"Odongo")
        self.assertEqual(self.new_credential.usr,"Andrew")
        self.assertEqual(self.new_credential.password,"37939509")
        self.assertEqual(self.new_credential.email,"drewodongo470@gmail.com")

    def test_save_credential(self):

         Credential.credential_list.append(self)

    def tearDown(self):

        Credential.credential_list =[]   

    def test_delete_credential(self):

        self.new_credential.save_credential()
        test_credential = Credential.credential("Test","user","37939509","test@user.com")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_credential_name(self):
                    

        self.new_credential.test_save_credential()
        test_credential =Credential("Test","user","0740478651","test@user.com")
        test_credential.save_credential()

        found_credential = Credential.find_name_by_name("Test")

        self.assertEqual(found_credential.email,test_credential.email)



    def test_credential_exists(self):


        self.new_credential.save_credential()
        test_Credential("Test","user","0740478651","test@user.com")
        test.credential.save_credential()

        credential_exists = Credential.credential_exist("0740478651")
        self.assertTrue(credential_exists)


if __name__ == '__main__':
    unittest.main()           