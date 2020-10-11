# def square(num): return num ** 2 #num>>number

square =  lambda num: num ** 2

numbers = [1,3,5,9,10,4]
result = tuple(map(lambda num: num ** 2, numbers))# aşağıdaki forun yaptığı işi yapar ve fonksiyona gerek kalmaz
# result = list(map(square, numbers))# aşağıdaki forun yaptığı işi yapar
# result = square(11)# direk isteğimiz herhangi bir sayınında karesi alabiliriz.
print(result)

for item in map(square, numbers):
    print(item)

# def check_even(num): return num%2==0
check_even = lambda num: num%2==0

# result = list(filter(check_even, numbers))
result = list(filter(lambda num: num%2==0, numbers))
result = list(map(lambda num: num%2==0, numbers))
result = list((lambda num: num%2==0, numbers))
# result = list(filter(check_even, numbers))
# result =list(filter(add,list(map(square,numbers))))
# result=list(filter(add,list(map(lambda num:num**3,numbers))))
#result=list(filter(add,list(map(lambda num:num**3,[1,2,3,4,5,6,8]))))
# result = check_even(numbers[2])


# print(result)
