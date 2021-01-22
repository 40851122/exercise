x1 = eval(input('x1:'))
y1 = eval(input('y1:'))
x2 = eval(input('x2:'))
y2 = eval(input('y2:'))

coordinate1 = (x1,y1)
coordinate2 = (x2,y2)
Distance = (((x1 - x2)**2) + ((y1 - y2)**2))**0.5
print(coordinate1)
print(coordinate2)
print(F'Distance = {Distance:0.4f}')