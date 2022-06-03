from random import randint

if __name__ == '__main__':

	P = 18
	
	G = 5
	
	
	print('The Value of P is :%d'%(P))
	print('The Value of G is :%d'%(G))
	
	a = 9
	print('The Private Key a for board1 is :%d'%(a))
	
	x = int(pow(G,a,P))
	
	b = 7
	print('The Private Key b for board2 is :%d'%(b))
	
	y = int(pow(G,b,P))
	
	
	ka = int(pow(y,a,P))
	
	kb = int(pow(x,b,P))
	
	print('Symmetric key is : %d'%(ka))
