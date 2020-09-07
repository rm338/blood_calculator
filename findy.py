def find_y(point1, point2, x3):
    slope = find_slope(point1,point2)
    return ((slope*(x3-point2[0])) + point2[1])

def find_slope(point1, point2):
    return (point2[1]-point1[1])/(point2[0]-point1[0])

