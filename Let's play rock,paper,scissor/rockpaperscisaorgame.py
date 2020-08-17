
import random
attempts = 0
c = 0
d = 0
e = 0
choices = ['r','p','s']

print('Welcome to the rock,paper,scissor competition')

while attempts < 10 :
	guess = input('For rock press r\nFor paper press p\nFor Scissor press s\n')
	b = random.choice(choices)
	attempts += 1
	if (guess == 'r' and b == 's' ) or (guess == 'p' and b == 'r' ) or (guess == 's' and b == 'p' ):
		print('Congratulations you won this round')
		c += 1
	elif (guess == b):
		print('Round drawn')
		d += 1
	else :
		print('You lost, Better luck next time')
		e += 1 
print('game over')
print(f'Your score: {c}\nComputer score: {e}\nTotal drawn: {d}')
if (c == e):
	print('Competition tied')
elif (c > e):
	print('you won the competition')
else :
	print('you lost this competition')
	
	
	
