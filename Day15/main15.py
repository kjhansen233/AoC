#####################################
#DAY 15 DAY 15 DAY 15 DAY 15 DAY 15 #
#####################################
def checkForZeros(input):
	if 0 in input:
		return 0
	return 1

def main():
	#Sprinkles:		2,  0,  -2,  0,  3
	#Butterscotch:	0,  5,  -3,  0,  3
	#Chocolate:  	0,  0,   5, -1,  8
	#Candy:  		0, -1,   0,  5,  8

	#       Sprinkles     Butters    Chocolate    Candy  
	ingred=[2,0,-2,0,3],[0,5,-3,0,3],[0,0,5,-1,8],[0,-1,0,5,8]
	# [capacity, durability, flavour, texture, calories] 

	myperms=[];first = 1;
##### Initialize list of permutations #####
	overall = 0
	while first < 100:
		second = 100-first
		while second > 0:
			third = 100 - (first + second)
			while third > 0:
				fourth = 100 - (first + second + third)
				#if checkForZeros([first, second, third, fourth]) ==1:
				myperms.append([first, second, third, fourth])	
				overall+=1
				third -=1
			second -=1
		first +=1
	print "Loops to generate permutation: ",overall
	
	#initialize variables
	scoreCard = 0;tempScore =0;count = 0

##### Calculates Score #####
	while count < len(myperms):

	#initialize/reset variables for each loop
		subcount = 0;cap = 0;dur = 0;fla = 0;tex = 0;calories = 0
		while subcount < 4:
			#iterates over each ingredient, finding cap / dur / fla / tex / cal individually
			#then adds to running total for that permutation
			cap+=ingred[subcount][0]*myperms[count][subcount]
			dur+=ingred[subcount][1]*myperms[count][subcount]
			fla+=ingred[subcount][2]*myperms[count][subcount]
			tex+=ingred[subcount][3]*myperms[count][subcount]
			calories+=ingred[subcount][4]*myperms[count][subcount]
			subcount += 1
	
		#make sure it meets requirements
		if dur > 0:
			if cap > 0:
				if fla > 0:
					if tex > 0:
						if calories == 500:
							tempScore = dur*cap*fla*tex
		#test current score vs best score
		if tempScore > scoreCard:
			scoreCard = tempScore
			
		count+=1
	print "Best Score: ",scoreCard
		
main()