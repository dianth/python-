# a simple number guessing game

secretNumber = 6
totalChance = 3
chanceCount = 0

while chanceCount < totalChance :
     guess = int(input('guess your secret number:'))
     if guess == secretNumber:
         print('congratulations!! You Won')
         break
     else:
         print('wrong guess') 
else:
    print('you lost') 
