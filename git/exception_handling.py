#try catch blocks are used to handle the errors
#that are raised in our programmes.
try:
    age = int(input('age: '))
    income = 20000
    risk = income / age
    print(risk)
    
except ZeroDivisionError:
    print('can not divide by 0' )
except ValueError:
    print('invalid value! ')