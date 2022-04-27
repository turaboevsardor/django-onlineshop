all_products = {'ves sklad':{}}
korzina = []
while True:
    admin = input('nima kerak')
    if admin == 'qoshish':
        product_name = input('productni ismi')
        product_count = input('productni soni')
        all_products['ves sklad'][product_name] = product_count
    elif admin == 'savadga':
            chto_kupit = input('savadga')
            korzina.append(chto_kupit)
            print(korzina)
    elif admin == 'ves sklad':
            print(all_products)
