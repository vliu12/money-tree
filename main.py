from cmu_graphics import *
from tree import *
from tod import *

def onAppStart(app):
    app.background = "lightblue"
    app.width = 617
    app.height = 1257
    app.timeOfDay = get_current_datetime()
    app.backgroundImage = "images/homepage.png"
    app.imageWidth, app.imageHeight = getImageSize(app.backgroundImage)
    print(app.imageWidth, app.imageHeight)

def onStep(app):
    app.stepsPerSecond = 60
    app.timeOfDay = get_current_datetime()



def redrawAll(app):
    drawRect(0, 0, app.width, app.height,  fill = app.background)
    drawLabel(app.timeOfDay.time, app.width/2, app.height/2, font = "Arial", size = 40, fill = "black")
    drawImage(app.backgroundImage, 0, 0, width=app.imageWidth, height=app.imageHeight,
          opacity=100, rotateAngle=0, align='left-top', visible=True)

runApp(width=app.width, height=app.height)