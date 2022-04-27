# cafe = {'evos':{}}
#
# cafe['evos']['address'] = 'toshmi'
#
# print(cafe)


# bayramlar = {}
# kun = input('kunini yoz')
#
# navruz = input('21-mart')
# bayramlar = input('navruz')
#
# print(bayramlar.items)












karzinka = {"karzina":{}}
shop = {'produktalar':{}}
while True:
    admin = input('nima kerak')
    if admin == 'qoshish':
        product_name = input('productni ismini yozin')
        product_count = input('productni soni')
        shop['produktalar'][product_name] = product_count
    elif admin == 'productlar':
        print(shop)
    elif
