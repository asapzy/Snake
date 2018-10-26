import math 

def setup():
    size(1048,1048)
    global myFaceCoordinate
    global foodx
    global foody
    global direction
    global img
    img = loadImage("pattern.jpg")
    direction="up"
    foodx=800
    foody=350

    myFaceCoordinate = [[400,500],[450 , 500],[500,500],[500,550],[550,550]]

                  
def draw():
    global img
    background(255)
    image(img,0,0,1048,1048)
    drawBorder()
    drawFaces()
    drawFood(foodx,foody)
    move()
# SETTING ARROW KEY MOVEMENTS    
def keyPressed():
    global myFaceCoordinate
    global foodx
    global foody
    global direction
    if key == CODED:
        if keyCode== UP:
            direction = "up"
        if keyCode==DOWN:
            direction = "down" 
        if keyCode==RIGHT:
            direction = "right" 
        if keyCode==LEFT:
            direction = "left"
    # if facex == foodx and facey == foody:
    #     fill(255,0,0)
    #     ellipse(110,100,20,20)
    


    # #RANDOM PLACE FOOD ON SCREEN    
    #     foodx = int(random(0,1048))
    #     foody= int(random(0,1048))
    #     drawFood(foodx, foody)

# IF SNAKE TOUCHES BORDERS, EXIT GAME
  
        
        
# GROWING SNAKE SIZE




#FUNCTIONS
        
def drawBorder():
    fill(0)
    rect(0,0,1048,10)
    rect(0,10,10,1048)
    rect(10,1038,1048,10)
    rect(1038,10,10,1048)
    
def drawFaces():
     global myFaceCoordinate
     for body in myFaceCoordinate:
         drawFace(body[0], body[1])
def drawFace(x,y):
    fill(0)
    ellipse(x,y,50,50)
    fill(255)
    ellipse(x-9,y-10,15,15)
    ellipse(x+9,y-10,15,15)
    fill(0)
    ellipse(x + random(10), y - 10, 3, 3)
    ellipse(x - random(9), y - 10, 3, 3)
    


def drawFood(x,y):
    global foodx
    global foody
    fill(255,0,0)
    ellipse(foodx,foody,20,20)   
    
    
def collides( faceX, faceY, foodX, foodY): 
    global myFaceCoordinate
    faceRadius = 25
    foodRadius = 10
    distance = math.sqrt(math.pow(myFaceCoordinate[0][1]-foody, 2) + math.pow(myFaceCoordinate[0][0]-foodx,2))
    print(distance, (faceRadius + foodRadius))
    if distance < faceRadius + foodRadius:
        return True
    else:
        return False        

def move():
    global myFaceCoordinate
    myFaceCoordinate.pop()
    headx=myFaceCoordinate[0][0]
    heady=myFaceCoordinate[0][1]
    if direction =="up":
        myFaceCoordinate.insert(0,[headx,heady-50])
    if direction =="down":
        myFaceCoordinate.insert(0,[headx,heady+50])
    if direction =="right":
        myFaceCoordinate.insert(0,[headx+50,heady])
    if direction =="left":
        myFaceCoordinate.insert(0,[headx-50,heady])
    delay(50)
    if myFaceCoordinate[0][0] < 30 or myFaceCoordinate[0][0] > 1018 or myFaceCoordinate[0][1] < 30 or myFaceCoordinate[0][1] > 1018:
        exit()    
        
        
#CHECKING IF SNAKE & FOOD ARE TOUCHING, RANDOMIZING FOOD LOCATION        
    global myFaceCoordinate
    global foodx
    global foody
    if collides(myFaceCoordinate[0][0], myFaceCoordinate[0][1], foodx, foody) == True:
        lastBody=myFaceCoordinate[len(myFaceCoordinate)-1]
        lastBodyX=lastBody[0]
        lastBodyY=lastBody[1]
        if checkBodyParts(lastBodyX,lastBodyY-50) ==False:
            myFaceCoordinate.append([lastBodyX,lastBodyY-50])
        elif checkBodyParts(lastBodyX-50,lastBodyY) == False:
            myFaceCoordinate.append([lastBodyX-50,lastBodyY])
        elif checkBodyParts(lastBodyX, lastBodyY+50) == False:
            myFaceCoordinate.append([lastBodyX, lastBodyY+50])
        elif checkBodyParts(lastBodyX+50, lastBodyY)== False:
            myFaceCoordinate.append([lastBodyX+50, lastBodyY])
        else:
            myFaceCoordinate.append([lastBodyX,lastBodyY])
        foodx = int(random(0,1048))
        foody= int(random(0,1048))    
        
def checkBodyParts(x,y):
    for body in myFaceCoordinate:
        if body[0]==x and body[1]==y:
            return True
    return False
            
            
        
