# string = "Polytechnic"

# print("%s...%s", (string[0 : 3], string[len(string) - 3 : len(string)]))

# price = float(input("Enter a price: "))
# dollars = int(price)
# cents = int((price - dollars) * 100 + 0.5)

# print(dollars, "dollars", cents, "cents")
# print(f'{dollars} dollars {cents} cents')

# name = ['Fritz']
# name.insert(1, 'Ann')
# name.insert(0, 'Melina')
# name.pop(2)
# name.append('Jorge')
# name.sort()
# print(name)

contacts = { 'Jenny': 8675309, 'James': 5551212 }
print(*contacts)
print('Jenny number is', contacts['Jenny'])
brain =  contacts.get('James')
print('Brian has new number', brain)