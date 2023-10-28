names = ['john', 'jackline','kish', 'Bree']
names[0] = 'jon'#updates the value in index 0
print(names) #prints the whole list
print(names[0])#prints the value in index 0
print(names[-1])#prints the value of first index from the end of the list
print(names[2:]) #prints values from 2nd index to the last

# finding the max number i a list
numbers = [1,2,3,4,5,6,7,8]
max = numbers[0] #max no. is set to the first in the list
for num in numbers:
    if num > max: #the for loop iterates throuh
        #the second number in the list
        #and checks if it is greater than the 1st
        #one,if it is,it is set to the max number,repeated till the max is found
        max = num #if found, num is set to max and printed
print(max)

#.upper()- converts characters to uppercase
#.lower()-converts characters to lowercase
#.find()-returns the index of a specified character in a string
#.replace()-replaces a specified character or a whole string
#synthax(print(x.replace('i','j')))
#in- bolean operator for finding a character in a string or a string in a string
#syntax(print('x' in y))