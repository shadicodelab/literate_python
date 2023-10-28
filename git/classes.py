class point:
    #creating a constructor that creates an object 
    #x and y and calls the parameters of the objects. 
    def __init__(self, x, y):
        self.x = x#initializing objects
        self.y = y
    #the move and start are methods of the class point   
    def move(self):
        print('move')
        
    def draw(self):
        print('draw')
        
#point1=point()#defining point1 object to refer to methods of class point.
#point1.draw()#calling the parameters of the method draw.

point=point(10, 20)#creating constructor objects
#point.x=20
print(point.x)
print(point.y)
        