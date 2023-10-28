def greet_user(fname, lname):#creating a function greet_user &passing two parameters,fname and lname
    print(f'{fname} {lname}!')
    print('welcome abroad')
    
    
print('start')
greet_user('john', 'smith')#calling the function and adding an argument on the parameter
greet_user(fname='Mary', lname='wangui')#adding keyword arguments
print('finish')

#return statement
def square(num):
    return num * num


print(square(4))