# range
# for item in range(50,100,20):
#     print(item)

# print(list(range(5,100,10)))

# enumerate

# greeting = 'Hello'

# for index, item in enumerate(greeting):
#     print(f'index: {index} letter: {item}')

# zip

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))#print(zip(list1, list2, list3)) şeklide yazılmıyor


for item in zip(list1, list2, list3):
    print(item)

lists=[(list1[i],list2[i],list3[i]) for i in range(len(list1))]
print(lists)

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)

