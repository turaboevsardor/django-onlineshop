# class Parents:
#     def __init__(self,name ,phone):
#          self.name = name
#          self.phone = phone
# class Son(Parents):
#      def __init__(self,name,phone,money):
#         super().__init__(name,phone)
#         self.money = money
# son1 = Son('alicho',123446,123)
# print(son1.money,-----------------------------828282822282)


# class Worker:
#     def __init__(self,name,position,exp):
#         self.name = name
#         self.position = position
#         self.exp = exp
# class Admin(Worker):
#     def __init__(self,name,position,exp):
#         super().__init__(name,position,exp)
#     def check(self,worker_name,worker_position):
#         return f'{worker_name} shetta ishlidi {worker_position}'
#
# jordan = Worker('jordan','injener','10 let')
# alex = Admin('alex','admin','234 let')
# print(alex.check('jordan',jordan.position))


class Player:
    def __init__(self,name,nomer,pz):
        self.name = name
        self.nomer = nomer
        self.pz = pz
class Xujumchi(Player):
    def __init__(self,name,nomer,pz,uslub):
        super().__init__(name,nomer,pz)
        self.uslub = uslub
    def hujumchi(self):
        return f'{self.name} yorvordi'

class Yarim_himoyachi(Player):
    def __init__(self,name,nomer,pz,uslub,):
        super().__init__(name,nomer,pz)
        self.uslub = uslub
    def yarim_himoyachi(self):
        return f'{self.name} ey gap yo'
class Himoyachi(Player):
    def __init__(self,name,nomer,pz,uslub,):
        super().__init__(name,nomer,pz)
        self.uslub = uslub
    def himoyachi(self):
        return f'{self.name} o may good'
class Darvozabon(Player):
    def __init__(self, name, nomer, pz, uslub, ):
        super().__init__(name, nomer, pz)
        self.uslub = uslub
    def darvozabon(self):
        return f'{self.name} qutqardi'

messi = Xujumchi('messi',10,'xujumchi','super')
pogba = Yarim_himoyachi('pogba',6,'yarim himoya','finter')
puyol = Himoyachi('puyol',5,'himoya','kuchli')
valdes = Darvozabon('valdes',1,'darvoza','agressiv')
print(messi.name,pogba.pz,puyol.nomer)


