secret_number = 9

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess=int(input('guess: '))
    guess_count+=1
    if guess== secret_number:
        print('You are a genius')
        break

else:
    print('you are a fool....!')
