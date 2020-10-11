# global scope
x = 'global x'

def function(): 
    # local scope
    x = 'local x'
    print(x)

function()
print(x)

####################

# global
name = 'Ahmet'

def changeName(new_name):
    global name
    name = new_name
    print(name)

changeName('Ada')
print(name)

####################

name = 'global string'

def greeting():
    name = 'Çınar'

    def hello():
        # name = 'Murat'
        print('hello '+ name)

    hello()

greeting()

####################

x = 70
def test(): 
    # global x
    x=50
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)

