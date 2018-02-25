import random
randnum = random.randint(1,100)
inputnum=input('Guess your number between 0 and 100  :  ')
num=int(inputnum)
print(randnum)
myguess=[0]
len(myguess)
while num !=randnum:
        if num < 1 or num >100:
            print ('\nNumber out of bounds')
            inputnum=input('Guess the number between 0 and 100  : ')
            num=int(inputnum)
            continue
        elif abs(randnum - num)>10 and len(myguess) == 1:
            myguess.append(num)
            print ('cold')
            inputnum=input('Guess the number  : ')
            num=int(inputnum)
            continue
        elif abs(randnum - num)<10 and len(myguess) == 1:
            myguess.append(num)
            print ('warm')
            inputnum=input('Guess the number  : ')
            num=int(inputnum)
            continue
        elif abs(randnum  - num) < abs(randnum - myguess[-1]):
            myguess.append(num)
            print ('warmer')
            inputnum=input('Guess the number  : ')
            num=int(inputnum)
            continue
        elif abs(randnum  - num) > abs(randnum- myguess[-1]):
            myguess.append(num)
            print ('colder')
            inputnum=input('Guess the number  : ')
            num=int(inputnum)
            continue
        elif num==randnum:
            print ('You guessed the number in % guesses'.format(len(myguess)+2) )
            break
print ('You guessed the number in {} guesses'.format(len(myguess)) )
