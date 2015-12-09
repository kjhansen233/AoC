#####################################
#DAY 2 DAY 2 DAY 2 DAY 2 DAY 2 DAY 2#
#####################################



def calculateWrapping(input):
	area = 0
	extra =0
	#Find first x value
	cIndex = input.find("x")
	#Dump start to x index into sub1
	sub1 = int(input[0:cIndex])
	
	#Strip out first segment, including first x
	input = input[cIndex+1:]
	#Find second x
	cIndex = input.find("x")
	
	#Dump start of new string to x into sub2
	sub2 = int(input[0:cIndex])
	
	#Dump from x+1 to end of string into sub3
	sub3 = int(input[cIndex+1:])
	
	if sub1 > sub2:
		if sub1 > sub3:
			extra = sub2*sub3
		else:
			extra = sub1*sub2
	elif sub2 > sub3:
		extra = sub1*sub3
	else:
		extra = sub1*sub2
	#Convert to numbers, apply calculations
	area = (2*sub1*sub2)+(2*sub1*sub3)+(2*sub2*sub3)+extra
		
	return area
	
def calculateRibbon(input):
	ribbon = 0
	bow =0
	total = 0
	#Find first x value
	cIndex = input.find("x")
	#Dump start to x index into sub1
	sub1 = int(input[0:cIndex])
	
	#Strip out first segment, including first x
	input = input[cIndex+1:]
	#Find second x
	cIndex = input.find("x")
	
	#Dump start of new string to x into sub2
	sub2 = int(input[0:cIndex])
	
	#Dump from x+1 to end of string into sub3
	sub3 = int(input[cIndex+1:])
	
	if sub1 > sub2:
		if sub1 > sub3:
			ribbon = (2*sub2)+(2*sub3)
		else:
			ribbon = (2*sub1)+(2*sub2)
	elif sub2 > sub3:
		ribbon = (2*sub1)+(2*sub3)
	else:
		ribbon = (2*sub1)+(2*sub2)

	bow = sub1*sub2*sub3
	total = bow + ribbon
		
	return total

input_file = open('input.txt', 'r')
input = input_file.read()
input_file.close()

count = 0
splitput=input.splitlines()
totalPaper = 0
totalRibbon = 0

while count < len(splitput):
	totalPaper+=calculateWrapping(splitput[count])
	totalRibbon+=calculateRibbon(splitput[count])
	count+=1
	
print "The total paper",totalPaper
print "The total ribbon",totalRibbon

output = open('output.txt', 'w')
output.write("teh fails")
output.close()