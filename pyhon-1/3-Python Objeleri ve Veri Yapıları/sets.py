fruits = { 'orange', 'apple', 'banana'}

# print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple'])

fruits.remove('mango')
fruits.discard('apple')
fruits.pop()#kümelerde listelerden farklı olarak ilk baştaki elemanı çıkarır. ve liste belirlenenden farklı random olarak gelir.

fruits.clear()

print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))
