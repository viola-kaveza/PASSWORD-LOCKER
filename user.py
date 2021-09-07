# import pyperclip
class User:

    user_list = []

    def __init__(self,account_name,user_name,pwd,e_address):



        self.first_name = account_name
        self.last_name = user_name
        self.user_name = pwd
        self.password = e_address

    user_list = []
    def delete_user(self):



        user.user_list.append(self)
    def save_user(self):



        User.user_list.append(self)
    @classmethod
    def find_by_user_name(cls,user_name):


        for user in cls.user_list:
            if user.user_name == user_name:
                return user_name
    @classmethod
    def user_exist(cls,user_name):

        for user in cls.user_list:
            if user.user_name == user_name:
                return True

        return False
    @classmethod
    def display_user(cls):

        return cls.user_list

    # @classmethod
    # def copy_password(cls,password):
    # user_found = user.find_by_password(password)
    # pyperclip.copy(user_found.password)