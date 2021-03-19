import math
x1=5
x2=10
y1=6
y2=3
a = math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
if a > 0:
	print("не симметричный")
elif a < 0:
	 print("не симметричный")
else:
	print("симметрик")