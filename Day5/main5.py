#####################################
#DAY 5 DAY 5 DAY 5 DAY 5 DAY 5 DAY 5#
#####################################

#####################################
#PART 1 PART 1 PART 1 PART 1 PART 1 #
#####################################

def checkVowels(input):
	vowels = 0
	count = 0
	while count < len(input):
		if input[count] == 'a' or input[count] == 'e' or input[count] == 'i' or input[count] == 'o' or input[count] == 'u':
			vowels +=1	
		count +=1
	if vowels >= 3:
		return 1
	return 0
	
	
def doubleLetter(input):
	count = 0
	while count < (len(input)-1):
		if input[count] == input[count+1]:
			return 1
		count+=1
	return 0

def noBadStrings(input):
	count = 0
	while count < (len(input)-1):
		if input[count] == 'a':
			if input[count+1] == 'b':
				return 0
				
		if input[count] == 'c':
			if input[count+1] == 'd':
				return 0	

		if input[count] == 'p':
			if input[count+1] == 'q':
				return 0	

		if input[count] == 'x':
			if input[count+1] == 'y':
				return 0	
		count+=1
	return 1

#####################################
#Part 2 Part 2 Part 2 Part 2 Part 2 #
#####################################	

def findPairs(input):
	cIndex = 0
	count = 0
	subStr =""
	while count < (len(input)-2):
		subStr = input[count]+input[count+1]
		cIndex=input.find(subStr, count+2)
		if cIndex > 0:
			return 1
		count+=1
	return 0

def repeatLetter(input):
	count = 0
	while count < (len(input)-2):
		if input[count] == input[count+2]:
			return 1
		count+=1
	return 0

	
	
input_file = open('input.txt', 'r')
input = input_file.read()
input_file.close()

splitput=input.splitlines()
nice = 0

count = 0
while count < len(splitput):
	#Part 1 Solution
	#if checkVowels(splitput[count]):
	#	if doubleLetter(splitput[count]):
	#		if noBadStrings(splitput[count]):
	#			nice+=1
	
	#Part 2 Solution
	if findPairs(splitput[count]):
		if repeatLetter(splitput[count]):
			nice +=1
	
	count+=1
	
print nice

#output = open('output.txt', 'w')
#output.write("teh fails")
#output.close()