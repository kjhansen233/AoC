#####################################
#DAY 6 DAY 6 DAY 6 DAY 6 DAY 6 DAY 6#
#####################################

def parseInstructions(cmd):
	#temporary variables
	tempIndex=0
	tempSubStr=""
	#used to build the command list
	op =""
	beginx=0
	beginy=0
	endx =0
	endy =0
	
	#pulls out which operation needs to be done, trims string to coords
	if cmd.find("turn on") == 0:
		op ="on"
		cmd = cmd[8:]
		
	elif cmd.find("turn off") == 0:
		op ="off"
		cmd = cmd[9:]
	else:
		op = "Tog"
		cmd = cmd[7:]
	
	#parse beginning coordinates
	tempsubStr=cmd[:cmd.find("t")-1]
	beginx = int(tempsubStr[:tempsubStr.find(",")])
	beginy = int(tempsubStr[tempsubStr.find(",")+1:])
	#remove middle 'through', leaving only end coords
	cmd= cmd[cmd.find("t")+8:]
	#pull end coords
	endx = int(cmd[:cmd.find(",")])
	endy = int(cmd[cmd.find(",")+1:])
		
	return [op, beginx, beginy, endx, endy]

input_file = open('input.txt', 'r')
input = input_file.read()
input_file.close()

splitput=input.splitlines()
matrix = [[0]]
xcount = 0
ycount = 0
command =['opperation','Bx','By','Ex','Ey']

#initialize Grid, all lights off
while xcount <=999:
	if xcount <999:
		matrix.append([0])
	while ycount < 999:
		matrix[xcount].append(0)
		ycount +=1
	ycount =0
	xcount+=1

#iterate through all commands
for item in splitput:
	command = parseInstructions(item)
	xcount = command[1]
	ycount = command[2]
	if command[0]== 'on':
		while xcount <= command[3]:
			while ycount <= command[4]:
				matrix[xcount][ycount] += 1
				ycount += 1
			ycount = command[2]
			xcount+=1
		
	elif command[0]== "off":
		while xcount <= command[3]:
			while ycount <= command[4]:
				if matrix[xcount][ycount]>0:
					matrix[xcount][ycount]-=1
				ycount += 1
			ycount = command[2]
			xcount+=1
	else:
		while xcount <= command[3]:
			while ycount <= command[4]:
				
				#if matrix[xcount][ycount]==1:
				#	matrix[xcount][ycount]=0
				#else:
				#	matrix[xcount][ycount]=1
				matrix[xcount][ycount]+=2
				ycount += 1
			ycount = command[2]
			xcount+=1

xcount = 0
ycount = 0
total = 0
while xcount <=999:
	while ycount <= 999:
		total += int(matrix[xcount][ycount])
		ycount +=1
	ycount =0
	xcount+=1			

print "Total Brightness:", total

#output = open('output.txt', 'w')
#output.write("teh fails")
#output.close()