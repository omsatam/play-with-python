#guess the number
import random
chances = 0
guesses = 10
a = random.randint(1,100)

 
while True:
 	b = int(input('enter the number: '))
 	chances += 1
 	if guesses < chances:
 		print('game over,better luck next time')
 		break
 	elif b == a :
 		print('Congratulations you nailed it')
 		print(f'you taken {chances} attemts')
 		break
 	elif a > b :
 		print('your number is too small,kindly try with larger number')
 	else:
 		print('your number is too big kindly try with smaller number')
 	
 
 		
