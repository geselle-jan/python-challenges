from Point import Point

x1 = 0
y1 = 0

x2 = 10
y2 = 10

p1 = Point(x1, y1)
p2 = Point(x2, y2)

print 'p1 = (' + str(x1) + ', ' + str(y1) + ')'
print 'p2 = (' + str(x2) + ', ' + str(y2) + ')'
print ''
print 'expected distance between p1 and p2 = 14,14...'
print 'computed distance between p1 and p2 = ' + str(p1.distance_to(p2))
print ''
print 'expected angle between p1 and p2 = 135.0'
print 'computed angle between p1 and p2 = ' + str(p1.angle_to(p2))