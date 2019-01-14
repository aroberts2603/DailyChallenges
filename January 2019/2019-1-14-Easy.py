# Given a string containing only the characters x and y, find whether there are the same number of xs and ys.
def balanced(str):
	xCounter = 0;
	yCounter = 0;
	for i in range(len(str)):
		if(str[i] == "x"):
			xCounter += 1
		elif(str[i] == "y"):
			yCounter += 1
	if(xCounter == yCounter):
		return True
	else:
		return False

print(balanced("xxxyyy"))#true
print(balanced("yyyxxx"))#true
print(balanced("xxxyyyy"))#false
print(balanced("yyxyxxyxxyyyyxxxyxyx"))#true
print(balanced("xyxxxxyyyxyxxyxxyy"))#false
print(balanced(""))#true
print(balanced("x"))#false