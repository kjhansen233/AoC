#####################################
#DAY 1 DAY 1 DAY 1 DAY 1 DAY 1 DAY 1#
#####################################

input_file = open('input.txt', 'r')
input = input_file.read()
input_file.close()

current_floor = 0
count = 0
x = len(input)
while count < x:
	if input[count] == '(':
		current_floor +=1
	if input[count] == ')':
		current_floor -=1
	if current_floor == -1:
		break
	count +=1

print count

output = open('output.txt', 'w')
output.write("teh fails")