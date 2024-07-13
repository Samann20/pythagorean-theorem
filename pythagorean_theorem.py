x1= float(input("enter the x_coordinate of the first point: "))
y1= float(input("enter the y-coordinate of the first point: "))
x2= float(input("enter the x-coordinate of the second point: "))
y2= float(input("enter the y-coordinate of the second point: "))

#compute the distance using pythagorean theorem
distance= ((x2 - x1) **2+ (y2 - y1) **2) **0.5

#output the result
print("the distance between the two point is:", distance)

