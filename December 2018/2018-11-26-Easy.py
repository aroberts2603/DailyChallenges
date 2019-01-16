def convert(red, green, blue):
	return ("#"+hex(red)[2:]+hex(green)[2:]+hex(blue)[2:]).upper()

print(convert(127,255,212))
print(convert(43,179,186))

def blend(hexes):
	averages = []
	for i in range(3):
		total = 0
		count = 0
		for item in hexes:
			x = int(item[((i+1)*2)-1:((i+1)*2)+1],16)
			count+=x
			total+=1
		averages.append(round(count/total))
	return convert(averages[0],averages[1],averages[2])

print(blend({"#E6E6FA", "#FF69B4", "#B0C4DE"}))