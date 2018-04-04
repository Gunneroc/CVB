import random
import itertools

def play(rand,guess):
	CowBull = [0,0]
	for i in range(0,len(rand)):
		if rand[i] == guess[i]:
			CowBull[0] += 1
		elif guess[i] in rand: 
			CowBull[1] += 1
	return CowBull

def Solve(allnums, rand):
	counter = 0
	for i in range(len(allnums)):
		counter += 1
		aswrd = str(allnums.pop())
		CowBull = play(str(rand), aswrd)
		
		if CowBull == [0,0]:
			bad = list(itertools.permutations([aswrd[0],aswrd[1],aswrd[2],aswrd[3]]))
			for i in range(0,len(bad)):
				bad[i] = int(''.join(bad[i]))
				if bad[i] in allnums:
					allnums.remove(bad[i])
				

		if CowBull[0] == 4:
			print(aswrd)
			print(counter)
			break
	return(aswrd,counter)


if __name__ == '__main__':
	CowBull = [0,0]
	rand = random.randint(1000,9999)
	print(rand)

	allnums = set(list(range(1000,10000)))

	print(len(allnums))
	Solve(allnums, rand)
	
	
