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

print("Basic:")
print(balanced("xxxyyy"))#true
print(balanced("yyyxxx"))#true
print(balanced("xxxyyyy"))#false
print(balanced("yyxyxxyxxyyyyxxxyxyx"))#true
print(balanced("xyxxxxyyyxyxxyxxyy"))#false
print(balanced(""))#true
print(balanced("x"))#false

# Optional Bonus - Given a string containing only lowercase letters
# find whether every letter that appears in the string appears the same number of times.

def advBalanced(string):
	letters = []
	counters = []
	for i in range(len(string)):
		if(not string[i] in letters):
			letters.append(string[i])
			counters.append(1)
		else:
			counters[letters.index(string[i])] += 1

	r = True
	for i in range(len(counters)-1):
		if(counters[i] != counters[i+1]):
			r = False

	return r

print("Advanced:")
print(advBalanced("xxxyyyzzz"))#True
print(advBalanced("abccbaabccba"))#True
print(advBalanced("xxxyyyzzzz"))#False
print(advBalanced("abcdefghijklmnopqrstuvwxyz"))#True
print(advBalanced("pqq"))#False
print(advBalanced("fdedfdeffeddefeeeefddf"))#False
print(advBalanced("www"))#True
print(advBalanced(""))#True
