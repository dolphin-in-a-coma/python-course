
def pentagon_sqare(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
    """function return value of square of pentagon
    
    arguments:(coordinates of pentagon's vertices)
		x1: float
		y1: float
		x2: float
		y2: float
		x3: float
		y3: float
		x4: float
		y4: float
		x5: float
		y5: float
		
	result:
		float"""

    def length_segment(x1,y1,x2,y2):
        """function return length of line segment
        
        arguments:(coordinates of pentagon's vertices)
			x1: float
			y1: float
			x2: float
			y2: float
		
		result:
			float
		"""
        #print(((x1-x2)**2+(y1-y2)**2)**0.5)
        return ((x1-x2)**2+(y1-y2)**2)**0.5

    def triangle_square(a,b,c):
        """function return value of square of triangle
        
        arguments:(length of sides)
			a: float
			b: float
			c: float
		
		result:
			float
        """
        p=(a+b+c)/2
        #print((p*(p-a)*(p-b)*(p-c))**0.5)
        return (p*(p-a)*(p-b)*(p-c))**0.5

    return (triangle_square(length_segment(x1,y1,x2,y2),
    length_segment(x3,y3,x2,y2),length_segment(x1,y1,x3,y3))+
    triangle_square(length_segment(x1,y1,x3,y3),
    length_segment(x3,y3,x4,y4),length_segment(x1,y1,x4,y4))+
    triangle_square(length_segment(x1,y1,x5,y5),
    length_segment(x5,y5,x4,y4),length_segment(x1,y1,x4,y4)))





params = [[float(i) for i in input('Enter separated by comma (x,y)\
 coordinates of {} pentagon\'s vertex: '.format(j+1)).split(sep=',')]
 for j in range(5)]
params=params[0]+params[1]+params[2]+params[3]+params[4]
print(pentagon_sqare(*params))
