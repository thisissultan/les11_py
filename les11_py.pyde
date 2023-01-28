
def setup():
    fullScreen();
    background(0, 0, 54)
    fill(0, 0, 100)
    rect(width / 4, height / 4, width / 2, width / 3)
    fill(0, 255, 0)
    rect(width / 4, height / 4 + height / 2, width / 35, width / 35)
    fill(255, 0, 0)
    rect(width / 4, height / 4 + height / 2 + 35, width / 35, width / 35)
    fill(0, 0, 255)
    rect(width / 4 + 40, height / 4 + height / 2, width / 35, width / 35)
    fill(255, 255, 0)
    rect(width / 4 + 40, height / 4 + height / 2 + 35, width / 35, width / 35)
    
def draw():

    fill(0, 0, 54)
    noStroke()
    #stroke(0, 255, 0)
    #strokeWeight(20)
    print(mouseButton)

    if mouseButton == 37:
        #point(mouseX ,mouseY)
        ellipse(mouseX, mouseY, 30, 30)
    if mouseButton == 3:
        background(0, 0, 54)

    

    




    
