
main_list = []

while True :

    item = input("Item (enter 'done' when finished): ")
    if item != "done":
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        item_dic = {}
        item_dic['item'] = item
        item_dic['price'] = price
        item_dic['Quantity'] = quantity
        main_list.append(item_dic)

    else:
        break

print("")
print('-'*25)
print("receipt")
print('-'*25)

for dict in main_list:
    print(dict['Quantity'] ,dict['item'] ,dict['Quantity']*dict['price'])