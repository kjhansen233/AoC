#####################################
#DAY 3 DAY 3 DAY 3 DAY 3 DAY 3 DAY 3#
#####################################

def dupCheck(houses, x, y):
	count = 0 
	coords = (x,y)
	while count < len(houses):
		if houses[count] == coords:
			print "Not adding",coords
			return 0
		count+=1
	print "Adding: ",coords
	return 1

input_file = open('input.txt', 'r')
input = input_file.read()
input_file.close()

santaOrRobo = 1
Sx=0
Sy=0
Rx=0
Ry=0
houses= [(Sx,Sy)]
print len(houses)
count = 0
z = len(input)

while count < z:
	if santaOrRobo:
		if input[count] == '^':	
			Sy += 1
		elif input[count] == 'v':
			Sy -= 1
		elif input[count] == '<':
			Sx -= 1
		else:
			Sx +=1
	
		if dupCheck(houses, Sx, Sy) ==1:
			houses.append((Sx, Sy))
		santaOrRobo = 0
	else:
		if input[count] == '^':	
			Ry += 1
		elif input[count] == 'v':
			Ry -= 1
		elif input[count] == '<':
			Rx -= 1
		else:
			Rx +=1
	
		if dupCheck(houses, Rx, Ry) ==1:
			houses.append((Rx, Ry))
		santaOrRobo =1 
	count +=1

	
print len(houses)
#output = open('output.txt', 'w')
#output.write("teh fails")
#output.close()