# class Person:
#     name = 'jordan '
#     age = 18
#     job = 'bussinesman'
#     weight = '61kg'
# print(Person.age,Person.weight)

# class Car:
#     def __init__(self,model,color,year):
#         self.model = model
#         self.color = color
#         self.year = year
# car1 = Car('spark','white',2022)
# car2 = Car('maluba','black',2022)
# car3 = Car('camaro','yellow',2019)
# print(car1.model,car1.color,car1.year)


# class Comment:
#     def __init__(self,username,text,likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
# while True:
#     users = input('ismini yoz ')
#     text = input('matnni yozin ')
#     user1 = Comment(users,text)
#     print(user1.text,user1.username)

# class Bank_accaunt:
#     def __init__(self,name,balance=0):
#         self.name = name
#         self.balance = balance

#     def deposit(self,new_cash):
#          self.balance += new_cash
#
#     def cash(self,cash):
#         self.balance -= cash
#
#     def balance(self):
#         print(self.balance)
#
# ali = Bank_accaunt('ali')
# print(ali.balance)
# print(ali.deposit(10))
# print(ali.cash(4))
# print(ali.balance)




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


