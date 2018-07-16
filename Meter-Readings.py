
readings = []

for x in range(1,6):
  reading = float(input("Enter reading number " + str(x) + ": "))
  readings.append(reading)

usage = readings[-1] - readings[0]

usages=[]
for x in range(1, len(readings)):
	usage = readings[x] - readings[x-1]
	if usage < 0:
		print("Error")
		quit()
	usages.append(usage)
	
	average = sum(usages)/len(usages)
	print("Your average usage is " + str(average))
	
cost = 3
print("Your cost per unit is " + str(cost) + "p")

totalCost = cost * usage
print("Total cost is " + str(totalCost) + "p")
