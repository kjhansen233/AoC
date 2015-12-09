#####################################
#DAY 4 DAY 4 DAY 4 DAY 4 DAY 4 DAY 4#
#####################################
import hashlib

input_file = open('input.txt', 'r')
input = input_file.read()
input_file.close()

count = 0
while count > -1:
	myhash = hashlib.md5("iwrupvqb"+str(count))
	digested = myhash.hexdigest()
	if digested[0:6] == '000000':
		break
	count+=1
	
print count

#output = open('output.txt', 'w')
#output.write("teh fails")
#output.close()