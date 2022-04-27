class User:
    def __init__(self,name,email,age,phone_number):
        self.name = name
        self.email = email
        self.age = age
        self.phone_number = phone_number
# user = User('alex','qwerty@mail',24,990777743)

    def change_name(self,new_name):
        self.name = new_name

    def change_email(self,new_email):
        self.email = new_email

    def change_phone_number(self,new_phone_number):
        self.phone_number = new_phone_number

user = User('jorj','jr@mail',24,999999999)
print(user.name,user.email)


