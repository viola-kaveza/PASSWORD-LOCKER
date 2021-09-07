import unittest
from password import Credential


class TestCredentials(unittest.TestCase):
    def SetUp(self):

        self.new_credential = Credential("Kaveza","Viola","Access","viola.kaveza@student.moringaschool.com") # create account object


    def test_init(self):


        self.assertEqual(self.new_credential.user_name,"Kaveza")
        self.assertEqual(self.new_credential.usr,"Viola")
        self.assertEqual(self.new_credential.password,"Access")
        self.assertEqual(self.new_credential.email,"viola.kaveza@student.moringaschool.com")

    def test_save_credential(self):

         Credential.credential_list.append(self)

    def tearDown(self):

        Credential.credential_list =[]   

    def test_delete_credential(self):

        self.new_credential.save_credential()
        test_credential = Credential.credential("Test","user","Access","test@user.com")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_credential_name(self):
                    

        self.new_credential.test_save_credential()
        test_credential =Credential("Test","user","0772308268","test@user.com")
        test_credential.save_credential()

        found_credential = Credential.find_name_by_name("Test")

        self.assertEqual(found_credential.email,test_credential.email)



    def test_credential_exists(self):


        self.new_credential.save_credential()
        test_Credential("Test","user","0740478651","test@user.com")
        test.credential.save_credential()

        credential_exists = Credential.credential_exist("0772308268")
        self.assertTrue(credential_exists)


if __name__ == '__main__':
    unittest.main()           