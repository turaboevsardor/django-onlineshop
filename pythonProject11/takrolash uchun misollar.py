# Создать переменную со значением integer
# a = [1,2,3,]
# print(a)
#
#
#
#
#
#
# # Создать переменную со значением string
# a = ["hello"]
# print(a)
#
#
#
#
#
#
#
#
#
#
# # Создать переменную со значением float
# a = [1.2,3.4]
# print(a)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Создать лист, который содержит в себе (int, str, tuple, list, dict)
# a = [1,"ali",("ali"),[122],{"name":"sardor"}]
# print(a)
#
#
#
#
#
#
#
#
#
#
#
#
# # Привести пример на list comprehension, который отбирает все слова, которые содержат букву d
# a = ['drum', 'danger', 'card', 'pasha', 'yard', 'crud', 'drug']
# s = list(filter(lambda l: "d" in l,a))
# print(list(s))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Создать примерный стэк юзера используя словарь
# q = {"user":"sardor",
#
#
#      "age":22,
#      "number":191919191}
# print(q)
#
#
#
#
#
# # Создать словарь, значение которого является другим словарем
# a = {"user":{}}
# a["user"]["nima"] = "sardor"
# print(a)
#
#
#
#
#
#
#
# # Используя цикл пройтись по списку и найти все имена с букыой 'd'
# a = ['drum', 'danger', 'card', 'pasha', 'yard', 'crud', 'drug']
#
# s = list(filter(lambda l: "d" in l,a))
# print(list(s))
#
#
#
#
#
#
#
#
# # Написать filter() функцию, которая проеверяет есть ли цифра 5 в списке
# a = [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,41214]
# s = list(filter(lambda k:k==5,a))
# print(s)
#
#
#
#
#
# # Отсортировать список, сделать его без повторяющихся элементов
# a = [1,2,3,3,4,5,5,5,6,7,8,9,9, 'Jordan', 'Pavel',
# 'Pasha', 'Kim', 'Drag', 'Messi', 'Ronaldo',
# 'Neymar', 'Jordan', 'Pavel', 'Pasha', 2,3,3,4,
# 'Kim', 'Drag','Drag', 'Messi', 'Ronaldo',
# 'Neymar', 'Jordan', 'Pavel', 'Pasha',]
# s = set(a)
# print(s)
#
#
#
#
#
#
#
#
#
#
#
# # Создать функцию которая проверяет есть ли некий элемент внутри списка
# def a(a="sardor"):
#     print(a)
# a("abl:")
#
#
#
#
#
#
#
#
#
#
# # Написать функцию с параметром, которая переворачивает текст
# print("damahum"[::-1])
#
# a = []
# i = input("vedite slova:  ")
# a.append(i[::-1])
# print(a)
#














## Задача 1 ##

##Напишите программу с классом Math.
#Создайте два атрибута — a и b.
#Напишите методы addition — сложение, multiplication — умножение,
#division — деление, subtraction — вычитание.
#При передаче в методы параметров a и b с ними нужно производить
#соответствующие действия и печатать ответ.
# class A:
#     def __init__(self,a,w):
#         self.a = a
#         self.w = w
#     def s(self):
#         return(self.a+self.w)
#     def w(self):
#         return(self.a-self.w)
# h = A(22,32)
# d = A(44,77)
# print(h.s())
# print(d.w())














## Задача 2 ##

## Напишите программу с классом Car.
#Создайте конструктор класса Car.
#Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
#Напишите пять методов.
#Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
#Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
#Третий — присвоение автомобилю года выпуска.
#Четвертый метод — присвоение автомобилю типа.
#Пятый — присвоение автомобилю цвета.
#
# class Playr:
#     def __init__(self,name,numb,pozit):
#         self.name = name
#         self.numb = numb
#         self.pozit = pozit
# class Nap(Playr):
#     def __init__(self,name,numb,pozit,talant):
#         super().__init__(name,numb,pozit)
#         self.talant = talant
#     def fast(self):
#         return f"{self.name}, haroshiy igra: "
# class Pol(Playr):
#     def __init__(self,name,numb,pozit,oyn):
#         super().__init__(name,numb,pozit)
#         self.oyn = oyn
#     def pas(self):
#         return f"{self.name}, haroshiy pas: "
# class Zash(Playr):
#     def __init__(self,name,numb,pozit,oynash):
#         super().__init__(name,numb,pozit)
#         self.oynash = oynash
#     def otb(self):
#         return f"{self.name},haroshi otbor"
# class Galk(Playr):
#     def __init__(self,name,numb,pozit,oyen):
#         super().__init__(name,numb,pozit)
#         self.oyen = oyen
#     def seyv(self):
#         return  f"{self.name}, haroshi seyv:"
# messi = Nap("messi",30,"napadayushi","fast")
# print(messi.pozit,messi.name,messi.numb,messi.talant)
# print(messi.fast())
# degon = Pol("dagon",14,"poluzashitnik","good game")
# print(degon.name,degon.pozit,degon.numb,degon.oyn)
# print(degon.pas())
# ramos = Zash("ramos",4,"zashitnik","good game")
# print(ramos.name,ramos.numb,ramos.pozit,ramos.oynash)
# print(ramos.otb())
# degeya = Galk("degeya",1,"galkiper","good game")
# print(degeya.name,degeya.pozit,degeya.numb,degeya.oyen)
# print(degeya.seyv())
#
#






