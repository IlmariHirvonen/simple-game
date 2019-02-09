
def player():
    forceY = forceY* drag
    forceX = forceX* drag
    if keyPressed:
        if key=='w':
            forceY=-5
        if forceY < -50:
            forceY= -50
        
        if key=='x':
            forceY=+5
        if forceY > 50:
            forceY= 50
        
        if key=='a':
            forceX=-5
        if forceX < -50:
            forceX= -50
        
        if key=='d':
            forceX=+5
        if forceX > 50:
            forceX = 50
    locX=locX+forceX
    locY=locY+forceY
    rect(locX-25,locY-25,50,50)
