#####################################
#DAY 8 DAY 8 DAY 8 DAY 8 DAY 8 DAY 8#
#####################################
import xml.sax.saxutils as saxutils


input_file = open('input.txt', 'r')
input = input_file.read()
input_file.close()

total = 0
splitput=input.splitlines()

#PART 1 PART 1 PART 1 
#for item in splitput:
#	total += len(item)-(len(item.decode('string_escape'))-2)
#print total


for item in splitput:
	modified = item.replace("\\", "\\\\")
	modified = modified.replace("\"", "\\\"")
	modified = "\""+ modified +"\""
	total += len(modified)-len(item)
	print modified
print total
	
		
	

