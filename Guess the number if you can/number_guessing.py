#guess the number
import random
c = 0
guesses = 5
a = random.randint(1,100)

 
while True:
 	b = int(input('enter the number'))
 	c += 1
 	if guesses < c:
 		print('game over')
 		break
 	elif b == a :
 		print('Congratulations you nailed it')
 		print(f'you taken {c} attemts')
 		break
 	elif a > b :
 		print('your number is too small,kindly try with larger number')
 	else:
 		print('your number is too big kindly try with smaller number')
 	
 
 		
#identify the guessed number
#print the no of iterations
